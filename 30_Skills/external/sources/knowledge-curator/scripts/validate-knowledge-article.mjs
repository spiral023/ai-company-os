#!/usr/bin/env node

import { createRequire } from 'node:module';
import {
  existsSync,
  realpathSync,
  readdirSync,
  readFileSync,
  statSync,
} from 'node:fs';
import { dirname, extname, join, relative, resolve, sep } from 'node:path';

const REQUIRED_FIELDS = [
  'title',
  'description',
  'type',
  'status',
  'category',
  'icon',
  'readTime',
  'tags',
  'aliases',
  'topics',
  'sourceURL',
  'sourceType',
  'addedDate',
];
const ENUMS = {
  type: new Set(['source']),
  status: new Set(['seed', 'incubating', 'evergreen', 'archived']),
  sourceType: new Set(['tweet', 'blog', 'thread', 'docs']),
  level: new Set(['beginner', 'intermediate', 'advanced']),
};
const ARRAY_FIELDS = ['tags', 'aliases', 'topics'];
const STRING_FIELDS = REQUIRED_FIELDS.filter((field) => (
  field !== 'readTime' && !ARRAY_FIELDS.includes(field)
));
const MERMAID_TYPES = new Set([
  'flowchart', 'graph', 'sequenceDiagram', 'classDiagram', 'stateDiagram',
  'stateDiagram-v2', 'erDiagram', 'journey', 'timeline', 'mindmap',
  'quadrantChart', 'xychart-beta', 'sankey-beta',
]);
const TRACKING_PARAMETERS = new Set([
  'fbclid', 'gclid', 'dclid', 'msclkid', 'mc_cid', 'mc_eid',
  '_ga', '_gl', 'igshid', 'ref', 'ref_src',
]);

function usage(message) {
  if (message) console.error(`Error: ${message}`);
  console.error(
    'Usage: node validate-knowledge-article.mjs <article.md> '
    + '[--project-root <path>] [--additional-source-count <n>] '
    + '[--allow-duplicate-source <existing-article.md>]...',
  );
  process.exit(2);
}

function parseArguments(argv) {
  let article;
  let projectRoot;
  let additionalSourceCount = 0;
  const allowedDuplicateSources = [];

  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === '--project-root') {
      if (projectRoot !== undefined) usage('--project-root darf nur einmal angegeben werden.');
      projectRoot = argv[++index];
      if (!projectRoot) usage('--project-root erwartet einen Pfad.');
    } else if (argument === '--additional-source-count') {
      const value = argv[++index];
      if (value === undefined || !/^\d+$/.test(value)) {
        usage('--additional-source-count erwartet eine nichtnegative ganze Zahl.');
      }
      additionalSourceCount = Number(value);
      if (!Number.isSafeInteger(additionalSourceCount)) {
        usage('--additional-source-count ist zu gross.');
      }
    } else if (argument === '--allow-duplicate-source') {
      const value = argv[++index];
      if (!value || value.startsWith('-')) {
        usage('--allow-duplicate-source erwartet einen Pfad als Wert.');
      }
      allowedDuplicateSources.push(resolve(value));
    } else if (argument.startsWith('-')) {
      usage(`Unbekannte Option: ${argument}`);
    } else if (article) {
      usage(`Unerwartetes Argument: ${argument}`);
    } else {
      article = argument;
    }
  }

  if (!article) usage('Der Pfad zu einem Artikel fehlt.');
  return {
    article: resolve(article),
    projectRoot,
    additionalSourceCount,
    allowedDuplicateSources,
  };
}

function findProjectRoot(articlePath, configuredRoot) {
  if (configuredRoot) {
    const root = resolve(configuredRoot);
    if (!existsSync(join(root, 'package.json'))) {
      usage(`Project root ${root} enthaelt keine package.json.`);
    }
    return realpathSync(root);
  }

  let current = existsSync(articlePath) && statSync(articlePath).isDirectory()
    ? articlePath
    : dirname(articlePath);
  while (true) {
    if (existsSync(join(current, 'package.json'))) return realpathSync(current);
    const parent = dirname(current);
    if (parent === current) break;
    current = parent;
  }
  usage(`Kein project root mit package.json oberhalb von ${articlePath} gefunden.`);
}

function loadGrayMatter(projectRoot) {
  try {
    const require = createRequire(join(projectRoot, 'package.json'));
    return require('gray-matter');
  } catch (error) {
    console.error(
      `Dependency error: gray-matter konnte ausgehend von ${projectRoot} nicht geladen werden. `
      + `Installiere die Dependency im Projekt. (${error.message})`,
    );
    process.exit(2);
  }
}

function displayPath(path, projectRoot) {
  const result = relative(projectRoot, path);
  return (result && !result.startsWith(`..${sep}`) && result !== '..' ? result : path)
    .split(sep).join('/');
}

function isPresent(value) {
  return value !== undefined && value !== null && (
    typeof value !== 'string' || value.trim() !== ''
  );
}

function isRealDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const [year, month, day] = value.split('-').map(Number);
  const date = new Date(Date.UTC(year, month - 1, day));
  return date.getUTCFullYear() === year
    && date.getUTCMonth() === month - 1
    && date.getUTCDate() === day;
}

function bodyWordCount(body) {
  const cleaned = body
    .replace(/!?(\[[^\]]*\])\([^\s)]+(?:\s+["'][^"']*["'])?\)/g, '$1')
    .replace(/https?:\/\/\S+/g, ' ')
    .replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, '$2 $1')
    .replace(/[\[\]#>*_`~|{}()!-]/g, ' ');
  return cleaned.match(/[\p{L}\p{N}]+(?:['’.-][\p{L}\p{N}]+)*/gu)?.length ?? 0;
}

function sectionContent(body, heading) {
  const escaped = heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = body.match(new RegExp(
    `^##[ \\t]+${escaped}[ \\t]*\\r?\\n([\\s\\S]*?)(?=^##[ \\t]+|(?![\\s\\S]))`,
    'im',
  ));
  return match?.[1]?.trim() ?? '';
}

function normalizeSourceUrl(value) {
  try {
    const url = new URL(value);
    if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) return null;
    url.hash = '';
    for (const name of [...url.searchParams.keys()]) {
      if (name.toLowerCase().startsWith('utm_') || TRACKING_PARAMETERS.has(name.toLowerCase())) {
        url.searchParams.delete(name);
      }
    }
    url.searchParams.sort();
    url.pathname = url.pathname.replace(/\/+$/, '') || '/';
    return url.toString().replace(/\/$/, '');
  } catch {
    return null;
  }
}

function markdownFiles(directory) {
  if (!existsSync(directory)) return [];
  const realDirectory = realpathSync(directory);
  const results = [];
  const seen = new Set();
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    if (!entry.name.toLowerCase().endsWith('.md')) continue;
    if (!entry.isFile() && !entry.isSymbolicLink()) continue;
    const path = join(directory, entry.name);
    let realPath;
    try {
      realPath = realpathSync(path);
    } catch (error) {
      usage(`Markdown-Datei/Symlink konnte nicht aufgeloest werden: ${path} (${error.message})`);
    }
    if (!pathIsInside(realDirectory, realPath)) {
      usage(`Markdown-Datei/Symlink liegt ausserhalb des Knowledge-Roots: ${path}`);
    }
    if (!statSync(realPath).isFile()) {
      usage(`Markdown-Datei/Symlink ist keine regulaere .md-Datei: ${path}`);
    }
    if (!seen.has(realPath)) {
      seen.add(realPath);
      results.push({ path, realPath });
    }
  }
  return results;
}

function filesRecursively(directory) {
  if (!existsSync(directory)) return [];
  const results = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) results.push(...filesRecursively(path));
    else if (entry.isFile() || entry.isSymbolicLink()) results.push(path);
  }
  return results;
}

function maskRange(text, start, end) {
  return `${text.slice(0, start)}${text.slice(start, end).replace(/[^\r\n]/g, ' ')}${text.slice(end)}`;
}

function maskRanges(text, ranges) {
  let masked = text;
  for (const [start, end] of [...ranges].sort((a, b) => b[0] - a[0])) {
    masked = maskRange(masked, start, end);
  }
  return masked;
}

function maskHtmlComments(body) {
  const ranges = [...body.matchAll(/<!--[\s\S]*?(?:-->|$)/g)].map((match) => (
    [match.index, match.index + match[0].length]
  ));
  return maskRanges(body, ranges);
}

function tokenizeFences(body) {
  const tokens = [];
  const linePattern = /[^\r\n]*(?:\r\n|\n|$)/g;
  let openFence;
  let line;
  while ((line = linePattern.exec(body)) !== null && line[0].length > 0) {
    const lineStart = line.index;
    const lineEnd = lineStart + line[0].length;
    const text = line[0].replace(/\r?\n$/, '');
    if (!openFence) {
      const opening = text.match(/^[ \t]*(`{3,}|~{3,})[ \t]*(.*?)[ \t]*$/);
      if (opening) {
        openFence = {
          start: lineStart,
          contentStart: lineEnd,
          marker: opening[1][0],
          markerLength: opening[1].length,
          info: opening[2].trim().split(/\s+/)[0]?.toLowerCase() ?? '',
        };
      }
    } else {
      const closing = text.match(/^[ \t]*(`{3,}|~{3,})[ \t]*$/);
      if (
        closing
        && closing[1][0] === openFence.marker
        && closing[1].length >= openFence.markerLength
      ) {
        tokens.push({
          ...openFence,
          contentEnd: lineStart,
          end: lineEnd,
          closed: true,
        });
        openFence = undefined;
      }
    }
  }
  if (openFence) {
    tokens.push({
      ...openFence,
      contentEnd: body.length,
      end: body.length,
      closed: false,
    });
  }
  return tokens;
}

function isEscaped(text, index) {
  let slashes = 0;
  for (let current = index - 1; current >= 0 && text[current] === '\\'; current -= 1) {
    slashes += 1;
  }
  return slashes % 2 === 1;
}

function maskInlineCode(body) {
  const ranges = [];
  for (let index = 0; index < body.length; index += 1) {
    if (body[index] !== '`' || isEscaped(body, index)) continue;
    let length = 1;
    while (body[index + length] === '`') length += 1;
    let closing = index + length;
    while (closing < body.length) {
      if (body[closing] !== '`' || isEscaped(body, closing)) {
        closing += 1;
        continue;
      }
      let closingLength = 1;
      while (body[closing + closingLength] === '`') closingLength += 1;
      if (closingLength === length) {
        ranges.push([index, closing + closingLength]);
        index = closing + closingLength - 1;
        break;
      }
      closing += closingLength;
    }
  }
  return maskRanges(body, ranges);
}

function maskEscapedMarkdownMarkers(body) {
  const characters = [...body];
  for (let index = 0; index < characters.length; index += 1) {
    if (characters[index] === '\\') {
      let runLength = 1;
      while (characters[index + runLength] === '\\') runLength += 1;
      const escapedIndex = index + runLength;
      if (runLength % 2 === 1 && ['!', '[', ']'].includes(characters[escapedIndex])) {
        characters[escapedIndex] = ' ';
      }
      index += runLength - 1;
    }
  }
  return characters.join('');
}

function analyzeRenderedMarkdown(body) {
  const commentsMasked = maskHtmlComments(body);
  const fences = tokenizeFences(commentsMasked);
  const fencesMasked = maskRanges(
    commentsMasked,
    fences.map((fence) => [fence.start, fence.end]),
  );
  return {
    fenceSource: commentsMasked,
    fences,
    renderedBody: maskEscapedMarkdownMarkers(maskInlineCode(fencesMasked)),
  };
}

function normalizeReferenceLabel(label) {
  return label.trim().replace(/\s+/g, ' ').toLowerCase();
}

function scanBracket(text, start) {
  let value = '';
  for (let index = start; index < text.length; index += 1) {
    if (text[index] === '\\' && index + 1 < text.length) {
      value += text[index + 1];
      index += 1;
    } else if (text[index] === ']') {
      return { value, end: index + 1 };
    } else {
      value += text[index];
    }
  }
  return null;
}

function scanInlineDestination(text, start) {
  let index = start;
  while (/\s/.test(text[index] ?? '')) index += 1;
  let target = '';

  if (text[index] === '<') {
    index += 1;
    while (index < text.length) {
      if (text[index] === '\\' && index + 1 < text.length) {
        target += text[index + 1];
        index += 2;
      } else if (text[index] === '>') {
        index += 1;
        break;
      } else {
        target += text[index++];
      }
    }
  } else {
    let depth = 0;
    while (index < text.length) {
      const character = text[index];
      if (character === '\\' && index + 1 < text.length) {
        target += text[index + 1];
        index += 2;
      } else if (character === '(') {
        depth += 1;
        target += character;
        index += 1;
      } else if (character === ')' && depth > 0) {
        depth -= 1;
        target += character;
        index += 1;
      } else if (character === ')' || (depth === 0 && /\s/.test(character))) {
        break;
      } else {
        target += character;
        index += 1;
      }
    }
  }

  let quote;
  let titleDepth = 0;
  while (index < text.length) {
    const character = text[index];
    if (character === '\\' && index + 1 < text.length) {
      index += 2;
    } else if (quote) {
      if (character === quote) quote = undefined;
      index += 1;
    } else if (character === '"' || character === "'") {
      quote = character;
      index += 1;
    } else if (character === '(') {
      titleDepth += 1;
      index += 1;
    } else if (character === ')' && titleDepth > 0) {
      titleDepth -= 1;
      index += 1;
    } else if (character === ')') {
      return { target, end: index + 1 };
    } else {
      index += 1;
    }
  }
  return null;
}

function extractMarkdownImages(body, diagnostics) {
  const definitions = new Map();
  const definitionPattern = /^[ \t]{0,3}\[([^\]]+)\]:[ \t]*(?:<([^>\r\n]*)>|([^\s]+))(?:[ \t]+(?:"[^"]*"|'[^']*'|\([^)]*\)))?[ \t]*$/gm;
  let match;
  while ((match = definitionPattern.exec(body)) !== null) {
    definitions.set(normalizeReferenceLabel(match[1]), match[2] ?? match[3]);
  }

  const images = [];
  for (let index = 0; index < body.length - 1; index += 1) {
    if (body[index] !== '!' || body[index + 1] !== '[') continue;
    const alt = scanBracket(body, index + 2);
    if (!alt) continue;
    if (body[alt.end] === '(') {
      const inline = scanInlineDestination(body, alt.end + 1);
      if (inline) {
        images.push({ alt: alt.value, target: inline.target });
        index = inline.end - 1;
      }
    } else if (body[alt.end] === '[') {
      const reference = scanBracket(body, alt.end + 1);
      if (!reference) continue;
      const label = reference.value || alt.value;
      const target = definitions.get(normalizeReferenceLabel(label));
      if (target === undefined) {
        diagnostics.push(`Markdown image reference "${label}" hat keine Definition.`);
      }
      images.push({ alt: alt.value, target });
      index = reference.end - 1;
    } else {
      const target = definitions.get(normalizeReferenceLabel(alt.value));
      if (target !== undefined) images.push({ alt: alt.value, target });
      index = alt.end - 1;
    }
  }
  return images;
}

function resolveLocalImage(target, projectRoot, slug) {
  const requiredPrefix = `/images/knowledge/${slug}/`;
  if (target.includes('?') || target.includes('#')) {
    return { error: 'ist invalid/ungueltig; Query und Fragment sind nicht erlaubt' };
  }
  if (!target.startsWith(requiredPrefix) || target.length === requiredPrefix.length) {
    return {
      error: `ist invalid/ungueltig; muss literal als heruntergeladener absoluter Pfad unter ${requiredPrefix} liegen`,
    };
  }
  if (
    /\\|[\u0000-\u001f\u007f]/.test(target)
    || /%(?:2f|5c|23|3f|0[0-9a-f]|1[0-9a-f]|7f)/i.test(target)
  ) {
    return { error: 'ist invalid/ungueltig; encodierte Separatoren oder Steuerzeichen sind nicht erlaubt' };
  }

  let decoded;
  try {
    decoded = decodeURIComponent(target);
  } catch {
    return { error: 'ungueltige URL-Kodierung' };
  }

  const publicImagesRoot = resolve(projectRoot, 'public', 'images');
  const articleImagesRoot = join(publicImagesRoot, 'knowledge', slug);
  const assetPath = resolve(projectRoot, 'public', `.${decoded}`);
  const relativePath = relative(articleImagesRoot, assetPath);
  if (
    relativePath === '..'
    || relativePath.startsWith(`..${sep}`)
    || resolve(relativePath) === relativePath
  ) {
    return { error: `Traversal ausserhalb von ${requiredPrefix} ist ungueltig` };
  }
  return {
    assetPath,
    articleImagesRoot,
    publicImagesRoot,
    publicRelative: relative(join(projectRoot, 'public'), assetPath),
  };
}

function pathIsInside(root, target) {
  const pathFromRoot = relative(root, target);
  return pathFromRoot !== '..'
    && !pathFromRoot.startsWith(`..${sep}`)
    && resolve(pathFromRoot) !== pathFromRoot;
}

function validateAllowedDuplicateSources(paths, projectRoot, articlePath) {
  if (paths.length === 0) return new Set();
  const knowledgeRoot = resolve(projectRoot, 'src', 'content', 'knowledge');
  let realKnowledgeRoot;
  let realArticlePath;
  try {
    realKnowledgeRoot = realpathSync(knowledgeRoot);
    realArticlePath = realpathSync(articlePath);
  } catch (error) {
    usage(`--allow-duplicate-source konnte Projektpfade nicht aufloesen: ${error.message}`);
  }

  const allowed = new Set();
  for (const configuredPath of paths) {
    if (extname(configuredPath).toLowerCase() !== '.md') {
      usage(`--allow-duplicate-source erwartet eine bestehende .md-Markdown-Datei: ${configuredPath}`);
    }
    if (!existsSync(configuredPath)) {
      usage(`--allow-duplicate-source Datei nicht gefunden: ${configuredPath}`);
    }

    let realPath;
    try {
      realPath = realpathSync(configuredPath);
      if (!statSync(realPath).isFile()) {
        usage(`--allow-duplicate-source ist keine regulaere Datei: ${configuredPath}`);
      }
    } catch (error) {
      usage(`--allow-duplicate-source ist nicht lesbar oder nicht aufloesbar: ${configuredPath} (${error.message})`);
    }
    if (!pathIsInside(realKnowledgeRoot, realPath)) {
      usage(`--allow-duplicate-source liegt ausserhalb von src/content/knowledge: ${configuredPath}`);
    }
    if (realPath === realArticlePath) {
      usage('--allow-duplicate-source darf nicht auf den Zielartikel selbst zeigen.');
    }
    allowed.add(realPath);
  }
  return allowed;
}

function resolveTrustedImageRoots(projectRoot, articleImagesRoot) {
  try {
    const realProjectRoot = realpathSync(projectRoot);
    const publicImagesRoot = resolve(projectRoot, 'public', 'images');
    if (!existsSync(publicImagesRoot)) return { missing: true };
    const realPublicImagesRoot = realpathSync(publicImagesRoot);
    if (
      realPublicImagesRoot === realProjectRoot
      || !pathIsInside(realProjectRoot, realPublicImagesRoot)
    ) {
      return { error: 'real public/images liegt ausserhalb des real project root' };
    }
    if (!existsSync(articleImagesRoot)) return { missing: true };
    const realArticleImagesRoot = realpathSync(articleImagesRoot);
    if (
      realArticleImagesRoot === realPublicImagesRoot
      || !pathIsInside(realPublicImagesRoot, realArticleImagesRoot)
    ) {
      return { error: 'realer Artikel-Assetordner liegt ausserhalb von real public/images' };
    }
    return { realProjectRoot, realPublicImagesRoot, realArticleImagesRoot };
  } catch (error) {
    return { error: `trusted Bild-Roots sind nicht lesbar oder invalid: ${error.message}` };
  }
}

function validateRealImageTarget(localImage, trustedRoots) {
  if (!isFile(localImage.assetPath)) return { missing: true };
  try {
    const realTarget = realpathSync(localImage.assetPath);
    if (
      !pathIsInside(trustedRoots.realPublicImagesRoot, realTarget)
      || !pathIsInside(trustedRoots.realArticleImagesRoot, realTarget)
      || !statSync(realTarget).isFile()
    ) {
      return { error: 'reales Symlink-/Bildziel liegt ausserhalb des Artikelordners oder ist invalid' };
    }
    return { realTarget };
  } catch {
    return { missing: true };
  }
}

function hasBytes(buffer, offset, expected) {
  return buffer.length >= offset + expected.length
    && expected.every((byte, index) => buffer[offset + index] === byte);
}

function validateImageContent(path, publicPath) {
  const extension = extname(publicPath).toLowerCase();
  if (extension === '.svg') {
    return 'SVG ist nicht erlaubt; bitte vor dem Speichern sicher in ein Rasterbild konvertieren';
  }
  const supported = new Set(['.png', '.jpg', '.jpeg', '.gif', '.webp', '.avif']);
  if (!supported.has(extension)) {
    return `nicht erlaubte Bild-Erweiterung ${extension || '(keine)'}`;
  }

  let contents;
  try {
    contents = readFileSync(path);
  } catch (error) {
    return `Bilddatei ist nicht lesbar: ${error.message}`;
  }
  if (contents.length === 0) return 'Bilddatei ist leer/empty';

  let matches;
  if (extension === '.png') {
    matches = hasBytes(contents, 0, [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
  } else if (extension === '.jpg' || extension === '.jpeg') {
    matches = hasBytes(contents, 0, [0xff, 0xd8, 0xff]);
  } else if (extension === '.gif') {
    matches = ['GIF87a', 'GIF89a'].includes(contents.subarray(0, 6).toString('ascii'));
  } else if (extension === '.webp') {
    matches = contents.subarray(0, 4).toString('ascii') === 'RIFF'
      && contents.subarray(8, 12).toString('ascii') === 'WEBP';
  } else if (extension === '.avif') {
    const boxSize = contents.length >= 4 ? contents.readUInt32BE(0) : 0;
    matches = contents.length >= 16
      && boxSize >= 16
      && boxSize <= contents.length
      && (boxSize - 16) % 4 === 0
      && contents.subarray(4, 8).toString('ascii') === 'ftyp';
    let hasAvifBrand = matches
      && /^(?:avif|avis)$/.test(contents.subarray(8, 12).toString('ascii'));
    for (let offset = 16; matches && !hasAvifBrand && offset + 4 <= boxSize; offset += 4) {
      if (/^(?:avif|avis)$/.test(contents.subarray(offset, offset + 4).toString('ascii'))) {
        hasAvifBrand = true;
      }
    }
    matches = matches && hasAvifBrand;
  }
  return matches ? null : `Dateityp/Signatur passt nicht zur Erweiterung ${extension}`;
}

function isFile(path) {
  try {
    return statSync(path).isFile();
  } catch {
    return false;
  }
}

function validateMermaid(fenceSource, fences, diagnostics) {
  for (const fence of fences.filter((item) => item.info === 'mermaid')) {
    if (!fence.closed) {
      diagnostics.push('mermaid Fence ist unclosed (ungeschlossen).');
      continue;
    }
    const contents = fenceSource.slice(fence.contentStart, fence.contentEnd).trim();
    const firstToken = contents.match(/^([^\s]+)/)?.[1];
    if (!firstToken || !MERMAID_TYPES.has(firstToken)) {
      diagnostics.push(
        `mermaid diagram type ${firstToken ? `"${firstToken}"` : '(leer)'} is unsupported.`,
      );
    }
  }
}

function validateArticle({
  articlePath,
  projectRoot,
  additionalSourceCount,
  allowedDuplicateSources,
  matter,
}) {
  const diagnostics = [];
  let parsed;
  try {
    parsed = matter(readFileSync(articlePath, 'utf8'));
  } catch (error) {
    diagnostics.push(`Artikel oder Frontmatter konnte nicht gelesen werden: ${error.message}`);
    return diagnostics;
  }
  const { data, content: body } = parsed;
  const markdown = analyzeRenderedMarkdown(body);
  const { renderedBody } = markdown;

  for (const field of REQUIRED_FIELDS) {
    if (!isPresent(data[field])) {
      const expectedType = STRING_FIELDS.includes(field) ? ' nonblank String/Text' : '';
      diagnostics.push(`${field}: required${expectedType} Pflichtfeld fehlt.`);
    }
  }
  for (const field of STRING_FIELDS) {
    if (isPresent(data[field]) && (typeof data[field] !== 'string' || data[field].trim() === '')) {
      diagnostics.push(`${field}: muss ein nonblank String/Text sein.`);
    }
  }
  for (const [field, accepted] of Object.entries(ENUMS)) {
    if (isPresent(data[field]) && !accepted.has(data[field])) {
      diagnostics.push(`${field}: unsupported/invalid value "${data[field]}".`);
    }
  }
  for (const field of ARRAY_FIELDS) {
    if (isPresent(data[field]) && (!Array.isArray(data[field]) || data[field].length === 0)) {
      diagnostics.push(`${field}: muss ein nichtleeres Array sein.`);
    } else if (Array.isArray(data[field])) {
      data[field].forEach((value, index) => {
        if (typeof value !== 'string' || value.trim() === '') {
          diagnostics.push(`${field}[${index}]: muss ein nonblank String/Text sein.`);
        }
      });
    }
  }
  if (Array.isArray(data.topics)) {
    data.topics.forEach((topic, index) => {
      if (typeof topic !== 'string' || !/^\[\[[^\]]+\]\]$/.test(topic)) {
        diagnostics.push(`topics[${index}]: muss ein String-Wikilink im Format [[...]] sein.`);
      }
    });
  }
  for (const field of ['addedDate', 'sourceDate']) {
    if ((field === 'addedDate' || isPresent(data[field])) && !isRealDate(data[field])) {
      diagnostics.push(`${field}: "${String(data[field])}" ist kein echtes Datum im Format YYYY-MM-DD.`);
    }
  }

  const expectedReadTime = Math.max(1, Math.ceil(bodyWordCount(renderedBody) / 140));
  if (isPresent(data.readTime) && (
    !Number.isInteger(data.readTime) || data.readTime !== expectedReadTime
  )) {
    diagnostics.push(
      `readTime: unplausible; erwartet ${expectedReadTime}, erhalten ${String(data.readTime)}.`,
    );
  }

  const normalizedUrl = isPresent(data.sourceURL) && typeof data.sourceURL === 'string'
    ? normalizeSourceUrl(data.sourceURL)
    : null;
  if (isPresent(data.sourceURL) && !normalizedUrl) {
    diagnostics.push(`sourceURL: invalid URL "${String(data.sourceURL)}".`);
  } else if (normalizedUrl) {
    const knowledgeDirectory = join(projectRoot, 'src', 'content', 'knowledge');
    const realArticlePath = realpathSync(articlePath);
    for (const { path: otherPath, realPath: realOtherPath } of markdownFiles(knowledgeDirectory)) {
      if (realOtherPath === realArticlePath) continue;
      if (allowedDuplicateSources.has(realOtherPath)) continue;
      try {
        const otherUrl = matter(readFileSync(otherPath, 'utf8')).data.sourceURL;
        if (typeof otherUrl === 'string' && normalizeSourceUrl(otherUrl) === normalizedUrl) {
          diagnostics.push(
            `sourceURL: duplicate/doppelt, bereits vorhanden in ${displayPath(otherPath, projectRoot)}.`,
          );
        }
      } catch {
        // An invalid unrelated article must not make this target impossible to validate.
      }
    }
  }

  const connections = sectionContent(renderedBody, 'Verbindungen');
  if (!connections) {
    diagnostics.push('Abschnitt ## Verbindungen ist required und darf nicht leer sein.');
  } else {
    const links = [...connections.matchAll(/\[\[([^\]]+)\]\]/g)]
      .map((item) => item[1].trim().toLowerCase());
    if (new Set(links).size < 2) {
      diagnostics.push('Abschnitt ## Verbindungen muss mindestens zwei einzigartige Wikilinks enthalten.');
    }
  }
  if (additionalSourceCount > 0 && !sectionContent(renderedBody, 'Quellen')) {
    diagnostics.push('Abschnitt ## Quellen ist bei additional sources required und darf nicht fehlen/leer sein.');
  }

  const slug = articlePath.split(/[\\/]/).pop().replace(/\.md$/i, '');
  const assetDirectory = join(projectRoot, 'public', 'images', 'knowledge', slug);
  const trustedImageRoots = resolveTrustedImageRoots(projectRoot, assetDirectory);
  if (trustedImageRoots.error) {
    diagnostics.push(`Bild-Assetordner ist ausserhalb trusted Roots oder invalid: ${trustedImageRoots.error}.`);
  }
  const referencedPublicPaths = new Set();
  for (const image of extractMarkdownImages(renderedBody, diagnostics)) {
    const alt = image.alt.trim();
    const target = image.target;
    if (!alt) diagnostics.push(`Markdown image ${target ?? '(ohne Ziel)'}: alt text darf nicht leer sein.`);
    if (typeof target !== 'string' || target.trim() === '') {
      diagnostics.push('Markdown image target/Ziel ist leer oder invalid/ungueltig.');
      continue;
    }
    const localImage = resolveLocalImage(target, projectRoot, slug);
    if (localImage?.error) {
      diagnostics.push(`Markdown image ${target}: ${localImage.error}.`);
    } else if (localImage) {
      referencedPublicPaths.add(localImage.publicRelative.toLowerCase());
      if (trustedImageRoots.error) continue;
      const realTarget = validateRealImageTarget(localImage, trustedImageRoots);
      if (realTarget.error) {
        diagnostics.push(`Markdown image ${target}: ${realTarget.error}.`);
      } else if (realTarget.missing) {
        diagnostics.push(`Markdown image missing/fehlt: ${target} ist nicht vorhanden.`);
      } else {
        const contentError = validateImageContent(realTarget.realTarget, localImage.assetPath);
        if (contentError) diagnostics.push(`Markdown image ${target}: ${contentError}.`);
      }
    }
  }

  if (!trustedImageRoots.error) {
    for (const assetPath of filesRecursively(assetDirectory)) {
      const publicRelative = relative(join(projectRoot, 'public'), assetPath).toLowerCase();
      if (!referencedPublicPaths.has(publicRelative)) {
        diagnostics.push(`Asset unreferenced/nicht referenziert: ${displayPath(assetPath, projectRoot)}.`);
      }
    }
  }

  validateMermaid(markdown.fenceSource, markdown.fences, diagnostics);
  return diagnostics;
}

const options = parseArguments(process.argv.slice(2));
if (!existsSync(options.article) || !statSync(options.article).isFile()) {
  usage(`Artikeldatei nicht gefunden: ${options.article}`);
}
const projectRoot = findProjectRoot(options.article, options.projectRoot);
const allowedDuplicateSources = validateAllowedDuplicateSources(
  options.allowedDuplicateSources,
  projectRoot,
  options.article,
);
const matter = loadGrayMatter(projectRoot);
const articleLabel = displayPath(options.article, projectRoot);
const diagnostics = validateArticle({
  articlePath: options.article,
  projectRoot,
  additionalSourceCount: options.additionalSourceCount,
  allowedDuplicateSources,
  matter,
});

if (diagnostics.length > 0) {
  console.error(`FAIL ${articleLabel}`);
  diagnostics.forEach((diagnostic) => console.error(`- ${diagnostic}`));
  process.exit(1);
}

console.log(`PASS ${articleLabel}`);
