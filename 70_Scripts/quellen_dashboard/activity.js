/* Reine Zeitreihenberechnung; wird beim HTML-Build eingebettet und läuft offline. */
function buildActivitySeries(rows, corpus, today, range = 'all') {
  const dayMs = 86400000;
  const iso = date => date.toISOString().slice(0, 10);
  const parse = value => {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(value || '')) return null;
    const date = new Date(value + 'T00:00:00Z');
    return Number.isFinite(date.getTime()) && iso(date) === value ? date : null;
  };
  const end = parse(today);
  if (!end) throw new Error('Ungültiges Enddatum');
  const dated = rows.filter(row => parse(row.captured) && row.captured <= today);
  const dates = corpus.map(row => row.captured).filter(value => parse(value) && value <= today).sort();
  if (!dates.length) return { items: [], start: '', end: today, total: 0, inRange: 0, baseline: 0, excluded: rows.length, grain: 'day' };
  const days = range === 'all' ? 0 : Number(range);
  if (range !== 'all' && (!Number.isInteger(days) || days < 1)) throw new Error('Ungültiger Zeitraum');
  // Gleiche Achse für alle Filter innerhalb eines Bestands.
  const start = days ? new Date(end.getTime() - (days - 1) * dayMs) : parse(dates[0]);
  const startIso = iso(start);
  const duration = Math.round((end - start) / dayMs) + 1;
  const grain = duration <= 31 ? 'day' : duration <= 180 ? 'week' : 'month';
  const counts = new Map();
  for (const row of dated) counts.set(row.captured, (counts.get(row.captured) || 0) + 1);
  const baseline = dated.filter(row => row.captured < startIso).length;
  let cumulative = baseline;
  const items = [];
  for (let cursor = new Date(start); cursor <= end;) {
    const next = new Date(cursor);
    if (grain === 'month') next.setUTCMonth(next.getUTCMonth() + 1, 1);
    else if (grain === 'week') next.setUTCDate(next.getUTCDate() + (7 - (next.getUTCDay() + 6) % 7));
    else next.setUTCDate(next.getUTCDate() + 1);
    const stop = new Date(Math.min(next.getTime() - dayMs, end.getTime()));
    let count = 0;
    for (let date = new Date(cursor); date <= stop; date = new Date(date.getTime() + dayMs)) count += counts.get(iso(date)) || 0;
    cumulative += count;
    items.push({ start: iso(cursor), end: iso(stop), count, cumulative });
    cursor = next;
  }
  return { items, start: startIso, end: today, total: dated.length, inRange: cumulative - baseline,
    baseline, excluded: rows.length - dated.length, grain };
}

if (typeof module !== 'undefined' && module.exports) module.exports = { buildActivitySeries };
