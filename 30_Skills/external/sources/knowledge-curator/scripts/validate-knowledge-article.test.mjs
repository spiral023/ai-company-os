import assert from 'node:assert/strict';
import {
  existsSync,
  linkSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  symlinkSync,
  writeFileSync,
} from 'node:fs';
import { dirname, join, parse, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const validatorPath = join(
  dirname(fileURLToPath(import.meta.url)),
  'validate-knowledge-article.mjs',
);

function isUsableRoot(candidate) {
  const packagePath = join(candidate, 'package.json');
  if (!existsSync(packagePath) || !existsSync(join(candidate, 'node_modules', 'gray-matter'))) {
    return false;
  }

  try {
    const packageJson = JSON.parse(readFileSync(packagePath, 'utf8'));
    return Boolean(
      packageJson.dependencies?.['gray-matter']
      || packageJson.devDependencies?.['gray-matter'],
    );
  } catch {
    return false;
  }
}

function findRoot(startDirectory = process.cwd()) {
  const configuredRoot = process.env.PROJECT_ROOT;
  if (configuredRoot) {
    const candidate = resolve(configuredRoot);
    if (isUsableRoot(candidate)) return candidate;

    throw new Error(
      `PROJECT_ROOT=${candidate} ist ungueltig: Erwartet wurden package.json `
      + 'mit deklarierter gray-matter-Dependency und node_modules/gray-matter.',
    );
  }

  let current = resolve(startDirectory);
  const { root: filesystemRoot } = parse(current);

  while (true) {
    if (isUsableRoot(current)) return current;

    if (current === filesystemRoot) break;
    current = dirname(current);
  }

  throw new Error(
    `Kein nutzbarer Projektroot oberhalb von ${startDirectory} gefunden. `
    + 'Setze PROJECT_ROOT auf ein Verzeichnis mit passender package.json und '
    + 'installiertem node_modules/gray-matter.',
  );
}

const Root = findRoot();

const defaultBody = `Kurzer Text fuer den Validator.

![Diagramm](/images/knowledge/testartikel/diagram.png)

## Verbindungen

- [[Codex]]
- [[Validation]]
`;

function yamlScalar(value) {
  if (typeof value === 'number') return String(value);
  return JSON.stringify(value);
}

function articleFixture({ fields = {}, omit = [], body = defaultBody } = {}) {
  const frontmatter = {
    title: 'Testartikel',
    description: 'Eine kurze Beschreibung fuer den Validator.',
    type: 'source',
    status: 'seed',
    category: 'tooling',
    icon: 'Code2',
    readTime: 1,
    tags: ['tooling/validation'],
    aliases: ['Validator-Test'],
    topics: ['[[Codex]]'],
    sourceURL: 'https://example.com/source',
    sourceType: 'docs',
    author: 'Ada Example',
    sourceDate: '2026-07-10',
    addedDate: '2026-07-11',
    level: 'intermediate',
    ...fields,
  };

  for (const key of omit) delete frontmatter[key];

  const lines = ['---'];
  for (const [key, value] of Object.entries(frontmatter)) {
    if (Array.isArray(value)) {
      lines.push(`${key}:`);
      for (const item of value) lines.push(`  - ${yamlScalar(item)}`);
    } else {
      lines.push(`${key}: ${yamlScalar(value)}`);
    }
  }
  lines.push('---', '', body);
  return lines.join('\n');
}

function writeText(path, content) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, content, 'utf8');
}

const MINIMAL_PNG = Buffer.from(
  'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=',
  'base64',
);

function writeBytes(path, content) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, content);
}

function createWorkspace(t, { article = articleFixture(), writeReferencedAsset = true } = {}) {
  const root = mkdtempSync(join(Root, '.tmp-knowledge-validator-'));
  t.after(() => rmSync(root, {
    recursive: true,
    force: true,
    maxRetries: 3,
    retryDelay: 100,
  }));

  writeText(
    join(root, 'package.json'),
    `${JSON.stringify({ private: true, type: 'module' }, null, 2)}\n`,
  );

  const articlePath = join(root, 'src', 'content', 'knowledge', 'testartikel.md');
  writeText(articlePath, article);

  if (writeReferencedAsset) {
    writeBytes(
      join(root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.png'),
      MINIMAL_PNG,
    );
  }

  return { root, articlePath };
}

function runValidator({ root, articlePath }, ...args) {
  const result = spawnSync(process.execPath, [validatorPath, articlePath, ...args], {
    cwd: root,
    encoding: 'utf8',
    timeout: 10_000,
  });

  assert.equal(result.error, undefined, `Validator konnte nicht gestartet werden: ${result.error}`);
  return {
    ...result,
    output: `${result.stdout ?? ''}\n${result.stderr ?? ''}`,
  };
}

function assertDiagnosticLine(output, expectedTerms) {
  const diagnosticLines = output.split(/\r?\n/).filter((line) => /^\s*-\s+/.test(line));
  const matchingLine = diagnosticLines.find((line) => (
    expectedTerms.every((term) => term.test(line))
  ));

  assert.ok(
    matchingLine,
    `Keine einzelne Diagnosezeile enthaelt alle Begriffe ${expectedTerms.join(', ')}.\n`
      + `Diagnosezeilen:\n${diagnosticLines.join('\n')}`,
  );
}

function assertRejected(result, expectedDiagnostics) {
  assert.equal(result.status, 1, `Validator sollte fachlich ablehnen. Ausgabe:\n${result.output}`);
  assert.match(result.output, /^FAIL\b.*$/m);
  for (const expectedTerms of expectedDiagnostics) {
    assertDiagnosticLine(result.output, expectedTerms);
  }
}

test('akzeptiert einen validen Artikel mit existierendem Bild', (t) => {
  const workspace = createWorkspace(t);

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('diagnostiziert fehlende Pflichtfelder und unsupported sourceType gemeinsam', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      fields: { sourceType: 'podcast' },
      omit: ['title', 'type'],
    }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/\btitle\b/i, /required|Pflicht|fehlt|missing/i],
    [/\btype\b/i, /required|Pflicht|fehlt|missing/i],
    [/\bsourceType\b/i, /unsupported|nicht unterst(?:ü|u)tzt|invalid/i, /\bpodcast\b/i],
  ]);
});

test('diagnostiziert ein invalides Datum und eine unplausible readTime gemeinsam', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      fields: { sourceDate: '2026-02-30', readTime: 99 },
    }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/\bsourceDate\b/i, /\b2026-02-30\b/i],
    [/\breadTime\b/i, /unplausible|plausib|expected|erwartet/i],
  ]);
});

test('diagnostiziert ein fehlendes referenziertes Bild und ein unreferenziertes Asset', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  writeText(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'orphan.png'),
    'unreferenced fixture image bytes',
  );

  const result = runValidator(workspace);

  assertRejected(result, [
    [/missing|fehlt|nicht vorhanden/i, /diagram\.png/i],
    [/unreferenced|nicht referenziert|verwaist/i, /orphan\.png/i],
  ]);
});

test('diagnostiziert eine doppelte normalisierte sourceURL und nennt die andere Datei', (t) => {
  const workspace = createWorkspace(t);
  writeText(
    join(workspace.root, 'src', 'content', 'knowledge', 'bestehender-artikel.md'),
    articleFixture({
      fields: {
        sourceURL: 'https://example.com/source/?utm_source=test&utm_medium=docs#section',
      },
    }),
  );

  const result = runValidator(workspace);

  assertRejected(result, [
    [/\bsourceURL\b/i, /duplicate|doppelt|bereits vorhanden/i, /bestehender-artikel\.md/i],
  ]);
});

test('fordert bei --additional-source-count 2 einen Abschnitt Quellen', (t) => {
  const workspace = createWorkspace(t);

  const result = runValidator(workspace, '--additional-source-count', '2');

  assertRejected(result, [
    [/Quellen|sources/i, /required|Pflicht|fehlt|missing/i],
  ]);
});

test('diagnostiziert einen ungeschlossenen mermaid-Fence', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: `${defaultBody}\n\n\`\`\`mermaid\ngraph TD\n  A --> B\n`,
    }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/\bmermaid\b/i, /ungeschlossen|unclosed|Fence/i],
  ]);
});

test('lehnt Topics mit aeusserem Whitespace ab', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({ fields: { topics: [' [[Codex]] '] } }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/topics\[0\]/i, /Wikilink|\[\[\.\.\.\]\]/i],
  ]);
});

test('erfasst angle-bracket Bildziele mit Leerzeichen', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: defaultBody.replace(
        '![Diagramm](/images/knowledge/testartikel/diagram.png)',
        '![](<\/images/knowledge/testartikel/fehlt mit leerzeichen.png>)',
      ),
    }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/alt text|Alt-Text/i, /leer|empty/i],
    [/missing|fehlt|nicht vorhanden/i, /fehlt mit leerzeichen\.png/i],
  ]);
});

test('erfasst reference-style Bilder und ihre Definitionen', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: defaultBody.replace(
        '![Diagramm](/images/knowledge/testartikel/diagram.png)',
        '![][diagram-ref]\n\n[diagram-ref]: /images/knowledge/testartikel/reference-fehlt.png',
      ),
    }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/alt text|Alt-Text/i, /leer|empty/i],
    [/missing|fehlt|nicht vorhanden/i, /reference-fehlt\.png/i],
  ]);
});

test('lehnt lokale Bildpfade mit Traversal ab, auch wenn das Ziel existiert', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: defaultBody.replace(
        '/images/knowledge/testartikel/diagram.png',
        '/images/../escape.png',
      ),
    }),
    writeReferencedAsset: false,
  });
  writeText(join(workspace.root, 'public', 'escape.png'), 'outside images fixture');

  const result = runValidator(workspace);

  assertRejected(result, [
    [/image|Bild/i, /Traversal|ausserhalb|unsafe|ungueltig|invalid/i, /escape\.png/i],
  ]);
});

test('akzeptiert ein Verzeichnis nicht als lokale Bilddatei', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  mkdirSync(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.png'),
    { recursive: true },
  );

  const result = runValidator(workspace);

  assertRejected(result, [
    [/image|Bild/i, /Datei|file|missing|fehlt|nicht vorhanden/i, /diagram\.png/i],
  ]);
});

test('diagnostiziert bei einem leeren Inline-Bild Alt-Text und Ziel gemeinsam', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: defaultBody.replace(
        '![Diagramm](/images/knowledge/testartikel/diagram.png)',
        '![]()',
      ),
    }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/alt text|Alt-Text/i, /leer|empty/i],
    [/image|Bild/i, /Ziel|destination|target/i, /leer|empty|ungueltig|invalid/i],
  ]);
});

test('diagnostiziert bei fehlender Bildreferenz Alt-Text und Definition gemeinsam', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      body: defaultBody.replace(
        '![Diagramm](/images/knowledge/testartikel/diagram.png)',
        '![][missing-ref]',
      ),
    }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/alt text|Alt-Text/i, /leer|empty/i],
    [/image|Bild/i, /missing-ref/i, /Definition|Referenz|reference/i, /fehlt|missing|keine/i],
  ]);
});

test('lehnt einen Bild-Symlink ab, dessen reales Ziel public/images verlaesst', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  const outsidePath = join(workspace.root, 'public', 'escape.png');
  const linkPath = join(
    workspace.root,
    'public',
    'images',
    'knowledge',
    'testartikel',
    'diagram.png',
  );
  writeText(outsidePath, 'outside images fixture');
  mkdirSync(dirname(linkPath), { recursive: true });
  try {
    symlinkSync(outsidePath, linkPath, 'file');
  } catch (error) {
    const junctionPath = join(dirname(linkPath), 'escape-link');
    try {
      symlinkSync(join(workspace.root, 'public'), junctionPath, 'junction');
      writeText(
        workspace.articlePath,
        articleFixture({
          body: defaultBody.replace(
            '/images/knowledge/testartikel/diagram.png',
            '/images/knowledge/testartikel/escape-link/escape.png',
          ),
        }),
      );
    } catch (junctionError) {
      t.skip(
        `Symlinks sind auf dieser Plattform nicht erlaubt: `
        + `${error.code ?? error.message}/${junctionError.code ?? junctionError.message}`,
      );
      return;
    }
  }

  const result = runValidator(workspace);

  assertRejected(result, [
    [/image|Bild/i, /Symlink|real/i, /ausserhalb|escape|Traversal|ungueltig|invalid/i],
  ]);
});

test('lehnt einen kompletten Artikel-Assetordner als Junction ausserhalb von public/images ab', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  const outsideDirectory = join(workspace.root, 'outside-assets');
  const assetDirectory = join(
    workspace.root,
    'public',
    'images',
    'knowledge',
    'testartikel',
  );
  writeBytes(join(outsideDirectory, 'diagram.png'), MINIMAL_PNG);
  mkdirSync(dirname(assetDirectory), { recursive: true });
  try {
    symlinkSync(outsideDirectory, assetDirectory, 'junction');
  } catch (error) {
    t.skip(`Junctions sind auf dieser Plattform nicht erlaubt: ${error.code ?? error.message}`);
    return;
  }

  const result = runValidator(workspace);

  assertRejected(result, [[
    /image|Bild/i,
    /real|Symlink|Junction|ausserhalb|outside|trusted|ungueltig|invalid/i,
  ]]);
});

test('ignoriert Verbindungen in Code-Fences und HTML-Kommentaren', (t) => {
  const body = `Text.

\`\`\`\`markdown
## Verbindungen
- [[Fence Eins]]
- [[Fence Zwei]]
\`\`\`\`

<!--
## Verbindungen
- [[Kommentar Eins]]
- [[Kommentar Zwei]]
-->
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/Verbindungen/i, /required|Pflicht|fehlt|missing/i],
  ]);
});

test('ignoriert Beispielbilder und Mermaid-Fences in nicht gerendertem Markdown', (t) => {
  const body = `Text.

\`\`\`\`markdown
![](/images/knowledge/testartikel/missing-fence.png)
\`\`\`mermaid
unsupportedDiagram
\`\`\`
\`\`\`\`

<!-- ![](/images/knowledge/testartikel/missing-comment.png) -->

## Verbindungen
- [[Codex]]
- [[Validation]]
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('parst balancierte Klammern und escapte Delimiter in Inline-Bildern', (t) => {
  const body = defaultBody.replace(
    '![Diagramm](/images/knowledge/testartikel/diagram.png)',
    String.raw`![Diagramm \] Version](/images/knowledge/testartikel/diagram_(v1).png)`,
  );
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });
  writeBytes(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram_(v1).png'),
    MINIMAL_PNG,
  );

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('lehnt sourceURL-Protokolle ausser http und https ab', (t) => {
  for (const sourceURL of [
    'javascript:alert(1)',
    'data:text/plain,test',
    'file:///tmp/source',
    'mailto:test@example.com',
  ]) {
    const workspace = createWorkspace(t, {
      article: articleFixture({ fields: { sourceURL } }),
    });
    const result = runValidator(workspace);
    assertRejected(result, [[/sourceURL/i, /invalid|ungueltig|http|https/i]]);
  }
});

test('lehnt Credentials in einer sourceURL ab', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      fields: { sourceURL: 'https://user:pass@example.com/source' },
    }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/sourceURL/i, /Credentials|Zugangsdaten|invalid|ungueltig/i],
  ]);
});

test('fordert nonblank Strings fuer erforderliche skalare Frontmatter-Felder', (t) => {
  const workspace = createWorkspace(t, {
    article: articleFixture({
      fields: {
        title: [],
        description: { text: 'object' },
        category: false,
        icon: 42,
        sourceType: true,
        addedDate: ['2026-07-11'],
      },
    }),
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/title/i, /String|Text/i],
    [/description/i, /String|Text/i],
    [/category/i, /String|Text/i],
    [/icon/i, /String|Text/i],
    [/sourceType/i, /String|Text/i],
    [/addedDate/i, /String|Text/i],
  ]);
});

test('validiert jedes Element in tags aliases und topics als nonblank String', (t) => {
  const invalidMembers = ['', 1, true, null, { object: true }, ['nested']];
  const workspace = createWorkspace(t, {
    article: articleFixture({
      fields: {
        tags: invalidMembers,
        aliases: invalidMembers,
        topics: [...invalidMembers, ' kein Wikilink '],
      },
    }),
  });

  const result = runValidator(workspace);

  const expected = [];
  for (const field of ['tags', 'aliases', 'topics']) {
    for (let index = 0; index < invalidMembers.length; index += 1) {
      expected.push([new RegExp(`${field}\\[${index}\\]`, 'i'), /nonblank|nichtleer|String|Text/i]);
    }
  }
  expected.push([/topics\[6\]/i, /Wikilink|\[\[\.\.\.\]\]/i]);
  assertRejected(result, expected);
});

test('ignoriert Bilder in Inline-Code und mit escaptem Markdown-Marker', (t) => {
  const body = `Text mit \`![](/images/knowledge/testartikel/inline-code-fehlt.png)\`.

\\![](/images/knowledge/testartikel/escaped-fehlt.png)

## Verbindungen
- [[Codex]]
- [[Validation]]
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('zaehlt Inline-Code und escapte Wikilinks nicht als Verbindungen', (t) => {
  const body = `Text.

## Verbindungen
- [[Echt]]
- \`[[Inline Code]]\`
- \\[[Escaped]]
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/Verbindungen/i, /mindestens|at least/i, /zwei|two|2/i, /Wikilink/i],
  ]);
});

test('laesst einen Fence-Marker im HTML-Kommentar spaetere Inhalte nicht maskieren', (t) => {
  const body = `<!-- Beispiel beginnt mit einem Fence:
\`\`\`markdown
-->

## Verbindungen
- [[Codex]]
- [[Validation]]
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('diagnostiziert einen unsupported Mermaid-Typ in einem Tilde-Fence', (t) => {
  const body = `${defaultBody}

  ~~~~ mermaid
unsupportedDiagram
  ~~~~
`;
  const workspace = createWorkspace(t, { article: articleFixture({ body }) });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/mermaid/i, /unsupported|invalid|nicht unterst/i, /unsupportedDiagram/i],
  ]);
});

test('diagnostiziert einen ungeschlossenen Mermaid-Tilde-Fence', (t) => {
  const body = `${defaultBody}

~~~mermaid
flowchart TD
  A --> B
`;
  const workspace = createWorkspace(t, { article: articleFixture({ body }) });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/mermaid/i, /ungeschlossen|unclosed|Fence/i],
  ]);
});

test('validiert Mermaid auch in einem Fence mit laengerem Marker', (t) => {
  const body = `${defaultBody}

\`\`\`\`\` mermaid
unsupportedLongFence
\`\`\`\`\`
`;
  const workspace = createWorkspace(t, { article: articleFixture({ body }) });

  const result = runValidator(workspace);

  assertRejected(result, [
    [/mermaid/i, /unsupported|invalid|nicht unterst/i, /unsupportedLongFence/i],
  ]);
});

test('schliesst alle erkannten Fence-Arten aus der readTime-Wortzahl aus', (t) => {
  const manyCodeWords = Array.from({ length: 160 }, (_, index) => `codewort${index}`).join(' ');
  const body = `Kurze gerenderte Prosa.

\`\`\`\`\`text
${manyCodeWords}
\`\`\`\`\`

~~~~text
${manyCodeWords}
~~~~

## Verbindungen
- [[Codex]]
- [[Validation]]
`;
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });

  const result = runValidator(workspace);

  assert.equal(result.status, 0, result.output);
});

test('fordert fuer jedes Markdown-Bild einen heruntergeladenen absoluten Zielpfad im Artikelordner', (t) => {
  const invalidTargets = [
    'https://example.com/image.png',
    '//example.com/image.png',
    'data:image/png;base64,iVBORw0KGgo=',
    'relative/image.png',
    '/images/knowledge/anderer-artikel/image.png',
  ];

  for (const target of invalidTargets) {
    const workspace = createWorkspace(t, {
      article: articleFixture({
        body: defaultBody.replace('/images/knowledge/testartikel/diagram.png', target),
      }),
      writeReferencedAsset: false,
    });
    if (target.startsWith('/images/knowledge/anderer-artikel/')) {
      writeBytes(
        join(workspace.root, 'public', 'images', 'knowledge', 'anderer-artikel', 'image.png'),
        MINIMAL_PNG,
      );
    }

    const result = runValidator(workspace);
    assertRejected(result, [[
      /Markdown image/i,
      /heruntergeladen|downloaded|absolut|absolute|Artikelordner|article directory|ungueltig|invalid/i,
    ]]);
  }
});

test('lehnt Query, Fragment und encodierte Separatoren oder Steuerzeichen in Bildzielen ab', (t) => {
  const invalidTargets = [
    '/images/knowledge/testartikel/diagram.png?cache=1',
    '/images/knowledge/testartikel/diagram.png#fragment',
    '%2Fimages%2Fknowledge%2Ftestartikel%2Fdiagram.png',
    '/images%2Fknowledge/testartikel/diagram.png',
    '/images/knowledge/testartikel/unterordner%2Fdiagram.png',
    '/images/knowledge/testartikel/unterordner%5Cdiagram.png',
    '/images/knowledge/testartikel/diagram%0A.png',
  ];

  for (const target of invalidTargets) {
    const workspace = createWorkspace(t, {
      article: articleFixture({
        body: defaultBody.replace('/images/knowledge/testartikel/diagram.png', target),
      }),
      writeReferencedAsset: false,
    });

    const result = runValidator(workspace);
    assertRejected(result, [[
      /Markdown image/i,
      /Query|Fragment|encod|Kodierung|Separator|Steuerzeichen|control|invalid|ungueltig/i,
    ]]);
  }
});

test('lehnt eine PNG-Datei mit Textinhalt ab', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  writeText(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.png'),
    'keine echten PNG-Bytes',
  );

  const result = runValidator(workspace);

  assertRejected(result, [[/diagram\.png/i, /Dateityp|file type|Signatur|signature|Inhalt|content/i]]);
});

test('lehnt eine Bilddatei ab, deren Inhalt nicht zur Erweiterung passt', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  writeBytes(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.png'),
    Buffer.from('GIF89a', 'ascii'),
  );

  const result = runValidator(workspace);

  assertRejected(result, [[/diagram\.png/i, /Erweiterung|extension|Dateityp|file type|Signatur|signature/i]]);
});

test('lehnt leere und nicht erlaubte lokale Bilddateien ab', (t) => {
  for (const [extension, bytes] of [['png', Buffer.alloc(0)], ['bmp', Buffer.from('BM', 'ascii')]]) {
    const body = defaultBody.replace('diagram.png', `diagram.${extension}`);
    const workspace = createWorkspace(t, {
      article: articleFixture({ body }),
      writeReferencedAsset: false,
    });
    writeBytes(
      join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', `diagram.${extension}`),
      bytes,
    );

    const result = runValidator(workspace);
    assertRejected(result, [[
      new RegExp(`diagram\\.${extension}`, 'i'),
      /leer|empty|Erweiterung|extension|Dateityp|file type|unsupported|nicht erlaubt/i,
    ]]);
  }
});

test('akzeptiert Signaturen aller erlaubten binaeren Bildtypen', (t) => {
  const fixtures = new Map([
    ['png', MINIMAL_PNG],
    ['jpg', Buffer.from([0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10])],
    ['jpeg', Buffer.from([0xff, 0xd8, 0xff, 0xe1, 0x00, 0x10])],
    ['gif', Buffer.from('GIF89a', 'ascii')],
    ['webp', Buffer.concat([Buffer.from('RIFF', 'ascii'), Buffer.alloc(4), Buffer.from('WEBP', 'ascii')])],
    ['avif', Buffer.concat([
      Buffer.from([0, 0, 0, 20]),
      Buffer.from('ftypmif1', 'ascii'),
      Buffer.alloc(4),
      Buffer.from('avif', 'ascii'),
    ])],
  ]);

  for (const [extension, bytes] of fixtures) {
    const body = defaultBody.replace('diagram.png', `diagram.${extension}`);
    const workspace = createWorkspace(t, {
      article: articleFixture({ body }),
      writeReferencedAsset: false,
    });
    writeBytes(
      join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', `diagram.${extension}`),
      bytes,
    );

    const result = runValidator(workspace);
    assert.equal(result.status, 0, `${extension}: ${result.output}`);
  }
});

test('lehnt auch ein sicheres SVG ab und verlangt Raster-Konvertierung', (t) => {
  const body = defaultBody.replace('diagram.png', 'diagram.svg');
  const workspace = createWorkspace(t, {
    article: articleFixture({ body }),
    writeReferencedAsset: false,
  });
  writeText(
    join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.svg'),
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1"><path d="M0 0h1v1z"/></svg>',
  );

  const result = runValidator(workspace);

  assertRejected(result, [[/diagram\.svg/i, /SVG/i, /Raster|konvert|convert/i]]);
});

test('lehnt aktive oder externe Inhalte in SVG-Dateien ohne stilles Sanitizing ab', (t) => {
  const unsafeSvgs = [
    '<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg"><path onload="alert(1)"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg"><foreignObject><div>HTML</div></foreignObject></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg"><image href="https://example.com/a.png"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><use xlink:href="//example.com/a.svg#x"/></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg"><a href="javascript:alert(1)"><path/></a></svg>',
    '<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,AA=="/></svg>',
  ];

  for (const svg of unsafeSvgs) {
    const body = defaultBody.replace('diagram.png', 'diagram.svg');
    const workspace = createWorkspace(t, {
      article: articleFixture({ body }),
      writeReferencedAsset: false,
    });
    writeText(
      join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.svg'),
      svg,
    );

    const result = runValidator(workspace);
    assertRejected(result, [[/diagram\.svg/i, /SVG/i, /Raster|konvert|convert/i]]);
  }
});

test('validiert die deklarierte AVIF-ftyp-Box statt Marker ausserhalb oder in malformed Boxen', (t) => {
  const invalidAvifs = [
    Buffer.concat([
      Buffer.from([0, 0, 0, 16]),
      Buffer.from('ftypmif1', 'ascii'),
      Buffer.alloc(4),
      Buffer.from('avif', 'ascii'),
    ]),
    Buffer.concat([
      Buffer.from([0, 0, 0, 24]),
      Buffer.from('ftypavif', 'ascii'),
      Buffer.alloc(8),
    ]),
    Buffer.concat([
      Buffer.from([0, 0, 0, 12]),
      Buffer.from('ftypavif', 'ascii'),
      Buffer.alloc(4),
    ]),
  ];

  for (const bytes of invalidAvifs) {
    const body = defaultBody.replace('diagram.png', 'diagram.avif');
    const workspace = createWorkspace(t, {
      article: articleFixture({ body }),
      writeReferencedAsset: false,
    });
    writeBytes(
      join(workspace.root, 'public', 'images', 'knowledge', 'testartikel', 'diagram.avif'),
      bytes,
    );

    const result = runValidator(workspace);
    assertRejected(result, [[/diagram\.avif/i, /AVIF|ftyp|Signatur|Dateityp|malformed|ungueltig/i]]);
  }
});

test('--allow-duplicate-source erlaubt exakt die angegebene Merge-Quelldatei', (t) => {
  const workspace = createWorkspace(t);
  const sourcePath = join(
    workspace.root,
    'src',
    'content',
    'knowledge',
    'merge-quelle.md',
  );
  writeText(sourcePath, articleFixture());

  const withoutAllowlist = runValidator(workspace);
  assertRejected(withoutAllowlist, [[/sourceURL/i, /duplicate|doppelt/i, /merge-quelle\.md/i]]);

  const withAllowlist = runValidator(workspace, '--allow-duplicate-source', sourcePath);
  assert.equal(withAllowlist.status, 0, withAllowlist.output);
});

test('--allow-duplicate-source bleibt fuer alle nicht freigegebenen Duplikate streng', (t) => {
  const workspace = createWorkspace(t);
  const knowledgeRoot = join(workspace.root, 'src', 'content', 'knowledge');
  const allowedPath = join(knowledgeRoot, 'merge-quelle.md');
  const thirdPath = join(knowledgeRoot, 'drittes-duplikat.md');
  writeText(allowedPath, articleFixture());
  writeText(thirdPath, articleFixture());

  const result = runValidator(workspace, '--allow-duplicate-source', allowedPath);

  assertRejected(result, [[/sourceURL/i, /duplicate|doppelt/i, /drittes-duplikat\.md/i]]);
});

test('--allow-duplicate-source ist wiederholbar', (t) => {
  const workspace = createWorkspace(t);
  const knowledgeRoot = join(workspace.root, 'src', 'content', 'knowledge');
  const firstPath = join(knowledgeRoot, 'merge-eins.md');
  const secondPath = join(knowledgeRoot, 'merge-zwei.md');
  writeText(firstPath, articleFixture());
  writeText(secondPath, articleFixture());

  const result = runValidator(
    workspace,
    '--allow-duplicate-source', firstPath,
    '--allow-duplicate-source', secondPath,
  );

  assert.equal(result.status, 0, result.output);
});

test('erkennt eine interne Markdown-Symlinkdatei als sourceURL-Duplikat', (t) => {
  const workspace = createWorkspace(t);
  const knowledgeRoot = join(workspace.root, 'src', 'content', 'knowledge');
  const realPath = join(knowledgeRoot, 'intern', 'echte-quelle.md');
  const linkPath = join(knowledgeRoot, 'verlinkte-quelle.md');
  writeText(realPath, articleFixture());
  try {
    symlinkSync(realPath, linkPath, 'file');
  } catch (error) {
    try {
      linkSync(realPath, linkPath);
    } catch (linkError) {
      t.skip(
        `Datei-Symlinks/Hardlinks sind nicht erlaubt: `
        + `${error.code ?? error.message}/${linkError.code ?? linkError.message}`,
      );
      return;
    }
  }

  const result = runValidator(workspace);

  assertRejected(result, [[/sourceURL/i, /duplicate|doppelt/i, /verlinkte-quelle\.md/i]]);
});

test('behandelt Markdown-Symlinks ausserhalb des Knowledge-Roots als operativen Fehler', (t) => {
  const workspace = createWorkspace(t);
  const outsidePath = join(workspace.root, 'outside-source.md');
  const linkPath = join(
    workspace.root,
    'src',
    'content',
    'knowledge',
    'outside-link.md',
  );
  writeText(outsidePath, articleFixture());
  try {
    symlinkSync(outsidePath, linkPath, 'file');
  } catch (error) {
    const outsideDirectory = join(workspace.root, 'outside-link-target');
    rmSync(outsidePath, { force: true });
    writeText(join(outsideDirectory, 'source.md'), articleFixture());
    try {
      symlinkSync(outsideDirectory, linkPath, 'junction');
    } catch (junctionError) {
      t.skip(
        `Datei-Symlinks/Junctions sind nicht erlaubt: `
        + `${error.code ?? error.message}/${junctionError.code ?? junctionError.message}`,
      );
      return;
    }
  }

  const result = runValidator(workspace);

  assert.equal(result.status, 2, result.output);
  assert.match(result.stderr, /outside-link\.md/i);
  assert.match(result.stderr, /ausserhalb|outside|knowledge/i);
});

test('eine leere Duplicate-Allowlist benoetigt keinen existierenden Knowledge-Ordner', (t) => {
  const workspace = createWorkspace(t, { writeReferencedAsset: false });
  rmSync(join(workspace.root, 'src'), { recursive: true, force: true });
  const articlePath = join(workspace.root, 'standalone.md');
  writeText(articlePath, articleFixture());

  const result = runValidator({ root: workspace.root, articlePath });

  assert.equal(result.status, 1, result.output);
  assert.doesNotMatch(result.stderr, /allow-duplicate-source/i);
  assert.match(result.stderr, /^FAIL\b/m);
});

test('ungueltige --allow-duplicate-source Werte sind operative Fehler', (t) => {
  const workspace = createWorkspace(t);
  const knowledgeRoot = join(workspace.root, 'src', 'content', 'knowledge');
  const outsideMarkdown = join(workspace.root, 'outside.md');
  const nonMarkdown = join(knowledgeRoot, 'quelle.txt');
  const missingMarkdown = join(knowledgeRoot, 'missing.md');
  writeText(outsideMarkdown, articleFixture());
  writeText(nonMarkdown, 'text');

  for (const [args, expectedReason] of [
    [['--allow-duplicate-source'], /erwartet|expects|Wert|value|Pfad|path/i],
    [['--allow-duplicate-source', missingMarkdown], /nicht gefunden|not found|exist/i],
    [['--allow-duplicate-source', outsideMarkdown], /ausserhalb|outside|knowledge/i],
    [['--allow-duplicate-source', nonMarkdown], /\.md|Markdown/i],
    [['--allow-duplicate-source', workspace.articlePath], /Ziel|target|Artikel selbst|itself/i],
  ]) {
    const result = runValidator(workspace, ...args);
    assert.equal(result.status, 2, `Erwartete operativen Exit 2 fuer ${args.join(' ')}:\n${result.output}`);
    assert.match(result.stderr, /Usage:/i);
    assert.match(result.stderr, /allow-duplicate-source/i);
    assert.match(result.stderr, expectedReason);
  }
});
