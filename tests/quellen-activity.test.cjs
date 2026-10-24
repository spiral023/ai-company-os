const { test } = require('node:test');
const assert = require('node:assert/strict');
const { buildActivitySeries } = require('../70_Scripts/quellen_dashboard/activity.js');
const rows = (...dates) => dates.map(captured => ({ captured }));

test('gesamte Historie einschließlich Quellen vor zwölf Wochen und heute', () => {
  const data = rows('2025-01-01', '2025-01-01', '2026-10-24');
  const series = buildActivitySeries(data, data, '2026-10-24');
  assert.equal(series.start, '2025-01-01');
  assert.equal(series.end, '2026-10-24');
  assert.equal(series.grain, 'month');
  assert.equal(series.items[0].count, 2);
  assert.equal(series.items.at(-1).cumulative, 3);
  assert.equal(series.items.reduce((n, item) => n + item.count, 0), 3);
  assert.equal(series.items.find(item => item.start === '2025-02-01').count, 0);
});

test('begrenzter Zeitraum startet mit kumuliertem Vorbestand und umfasst sieben Tage', () => {
  const data = rows('2026-01-01', '2026-10-17', '2026-10-18', '2026-10-24');
  const series = buildActivitySeries(data, data, '2026-10-24', '7');
  assert.equal(series.start, '2026-10-18');
  assert.equal(series.items.length, 7);
  assert.equal(series.baseline, 2);
  assert.equal(series.inRange, 2);
  assert.equal(series.items.at(-1).cumulative, 4);
});

test('Autorenfilter behalten die gemeinsame Zeitachse des Bestands', () => {
  const data = rows('2026-07-11', '2026-10-24');
  const series = buildActivitySeries([data[1]], data, '2026-10-24');
  assert.equal(series.start, '2026-07-11');
  assert.equal(series.total, 1);
  assert.equal(series.items[0].cumulative, 0);
  assert.equal(series.items.at(-1).cumulative, 1);
});

test('Monatsgrenzen, Schaltjahr und Zeitumstellung verlieren keine Tage', () => {
  const data = rows('2024-01-31', '2024-02-29', '2024-03-31', '2024-10-27');
  const series = buildActivitySeries(data, data, '2024-10-27');
  assert.equal(series.items[0].end, '2024-01-31');
  assert.equal(series.items[1].start, '2024-02-01');
  assert.equal(series.items[1].end, '2024-02-29');
  assert.equal(series.items.at(-1).cumulative, 4);
});

test('ungültige, fehlende und zukünftige Datumsangaben werden nicht erfunden', () => {
  const data = rows('', '2026-02-30', '2026-10-25', '2026-10-24');
  const series = buildActivitySeries(data, data, '2026-10-24');
  assert.equal(series.excluded, 3);
  assert.equal(series.total, 1);
  assert.equal(series.items.length, 1);
  assert.equal(buildActivitySeries([], [], '2026-10-24').items.length, 0);
  assert.throws(() => buildActivitySeries(data, data, '2026-10-24', 'invalid'));
});
