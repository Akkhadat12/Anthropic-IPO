// Centralized data module. Values mirror references/chart-data.csv and the claim ledger in 02_RESEARCH_AND_ANALYSIS.md.
// Research cutoff: 29 September 2026 (Thailand time). No public S-1 was available.

export const STATUS = {
  reported: { label: 'Reported · from filing seen by Reuters', short: 'Reuters · reported' },
  bloomberg: { label: 'Reported · Bloomberg, from investor documents', short: 'Bloomberg · reported' },
  prelim: { label: 'Preliminary · Bloomberg', short: 'Bloomberg · preliminary' },
  stated: { label: 'Anthropic stated', short: 'Anthropic stated' },
  bench: { label: 'Independent benchmark', short: 'Independent benchmark' },
  scenario: { label: 'Scenario · editorial analysis', short: 'Scenario' },
  unknown: { label: 'Not disclosed', short: 'Not disclosed' },
};

export const SRC = {
  reutersFiling: {
    id: 'S3',
    title: 'Reuters (via MarketScreener): Anthropic IPO prospectus report, 28 Sep 2026',
    url: 'https://www.marketscreener.com/news/anthropic-s-ipo-prospectus-shows-sweeping-ai-vision-surging-costs-ce785addd98afe2c',
    type: 'reported',
    caveat: 'Reporter saw a confidential draft. The document is not public and this team has not read it.',
  },
  reutersCommit: {
    id: 'S5',
    title: 'Reuters (via MarketScreener): $518B build-out hinges on deals that cannot be canceled, 29 Sep 2026',
    url: 'https://www.marketscreener.com/news/anthropic-s-518-billion-ai-buildout-hinges-largely-on-deals-that-cannot-be-canceled-filing-shows-ce785adddd8bf124',
    type: 'reported',
    caveat: 'Multi-year arrangements with different terms. Payment schedule and utilization are not public.',
  },
  bloombergQ2: {
    id: 'S4',
    title: 'Bloomberg: Anthropic revenue surges to over $11.5 billion in second quarter',
    url: 'https://news.bloomberglaw.com/artificial-intelligence/anthropic-revenue-surges-to-over-11-5-billion-in-second-quarter',
    type: 'prelim',
    caveat: 'Q1 ($4.73B) is reported from investor documents. Q2 (> $11.5B) is preliminary and may be revised. The adjusted Q2 result has no public reconciliation to GAAP.',
  },
  seriesH: {
    id: 'S2',
    title: 'Anthropic: Series H and May 2026 run-rate, 28 May 2026',
    url: 'https://www.anthropic.com/news/series-h',
    type: 'stated',
    caveat: 'Company statement. Run-rate is an annualized rate, not booked revenue. $965B is a private post-money valuation, not an IPO price.',
  },
  s1: {
    id: 'S1',
    title: 'Anthropic: confidential draft S-1 announcement, 1 Jun 2026',
    url: 'https://www.anthropic.com/news/confidential-draft-s1-sec',
    type: 'stated',
    caveat: 'Share count and price are not set. No public S-1 exists as of the research cutoff.',
  },
  awsCommit: {
    id: 'S9',
    title: 'Anthropic: Amazon compute agreement, 20 Apr 2026',
    url: 'https://www.anthropic.com/news/anthropic-amazon-compute',
    type: 'stated',
    caveat: 'AWS commitment of more than $100B over ten years may overlap with the $518B. Never add them.',
  },
  rainier: {
    id: 'A',
    title: 'AWS: Project Rainier (photographs)',
    url: 'https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster',
    type: 'stated',
    caveat: 'Photograph: Amazon Web Services. An AWS facility used for Anthropic workloads. Not an Anthropic-owned data center and not a measure of Anthropic capacity.',
  },
  axios: {
    id: 'S13',
    title: 'Axios: Anthropic and OpenAI revenue chasm explained, 3 Sep 2026',
    url: 'https://www.axios.com/2026/09/03/anthropic-and-openais-revenue-chasm-explained',
    type: 'reported',
    caveat: 'Reported gross vs net presentation through clouds. Channel mix and take rate are unknown.',
  },
  opus: {
    id: 'S11',
    title: 'Anthropic: Claude Opus 5.5, 22 Sep 2026',
    url: 'https://www.anthropic.com/claude-opus-5-5',
    type: 'stated',
    caveat: 'Company tests: about 40% lower typical-task cost than Opus 5. A different basis from the independent test.',
  },
  sonnet: {
    id: 'S12',
    title: 'Anthropic: Claude Sonnet 5.5, 28 Sep 2026',
    url: 'https://www.anthropic.com/claude-sonnet-5-5',
    type: 'stated',
    caveat: 'Company tests: up to 30% lower API cost per task than Sonnet 5 on its own test set.',
  },
  fable: {
    id: 'S10',
    title: 'Anthropic: Claude Fable 5.1 and Mythos 5.1, 1 Sep 2026',
    url: 'https://www.anthropic.com/claude-fable-and-mythos-5-1',
    type: 'stated',
    caveat: 'Mythos is available only to vetted groups. Haiku 5.5 is announced but not released.',
  },
  aaOpus: {
    id: 'S14',
    title: 'Artificial Analysis: Claude Opus 5.5, 22 Sep 2026',
    url: 'https://artificialanalysis.ai/articles/claude-opus-5-5',
    type: 'bench',
    caveat: 'Independent test: Intelligence Index 58 at max effort. Not provider serving cost or margin.',
  },
  aaSonnet: {
    id: 'S15',
    title: 'Artificial Analysis: Claude Sonnet 5.5, 28 Sep 2026',
    url: 'https://artificialanalysis.ai/articles/claude-sonnet-5-5',
    type: 'bench',
    caveat: 'Pre-release build; retest pending. Sonnet 5.5 max $7.60 vs Sonnet 5 max $5.09 per task on the same test. Not provider serving cost.',
  },
  googleBroadcom: {
    id: 'S8',
    title: 'Anthropic: Google and Broadcom compute partnership, 6 Apr 2026',
    url: 'https://www.anthropic.com/news/google-broadcom-partnership-compute',
    type: 'stated',
    caveat: 'Company compute strategy. Scenarios are editorial analysis, not a management forecast.',
  },
  ltbt: {
    id: 'S16',
    title: 'Anthropic: The Long-Term Benefit Trust',
    url: 'https://www.anthropic.com/news/the-long-term-benefit-trust',
    type: 'stated',
    caveat: 'Share rights and voting structure for an IPO must be read in the public S-1.',
  },
};

// Numeric manifest, mirrors references/chart-data.csv one-for-one.
export const DATA = {
  fy2025_revenue: { value: 4.6, op: '≈', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '≈ $4.6B' },
  q1_2026_revenue: { value: 4.73, op: '', unit: '$B', period: 'Q1 2026', status: 'bloomberg', src: 'bloombergQ2', text: '$4.73B' },
  q2_2026_revenue: { value: 11.5, op: '>', unit: '$B', period: 'Q2 2026', status: 'prelim', src: 'bloombergQ2', text: '> $11.5B' },
  may_2026_run_rate: { value: 47, op: '>', unit: '$B / year', period: 'May 2026', status: 'stated', src: 'seriesH', text: '> $47B / yr' },
  fy2025_operating_loss: { value: 8, op: '>', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '> $8B' },
  fy2025_net_loss: { value: 42, op: '≈', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '≈ $42B' },
  fy2025_noncash: { value: 34, op: '≈', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '≈ $34B' },
  fy2025_compute: { value: 7.33, op: '', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '$7.33B' },
  fy2025_opex: { value: 12.65, op: '', unit: '$B', period: 'FY2025', status: 'reported', src: 'reutersFiling', text: '$12.65B' },
  infra_arrangements: { value: 518, op: '≥', unit: '$B', period: '~ one decade', status: 'reported', src: 'reutersCommit', text: '≥ $518B' },
  noncancelable: { value: 80, op: '≈', unit: '% of arrangements', period: '~ one decade', status: 'reported', src: 'reutersCommit', text: '≈ 80%' },
  sonnet55_cost: { value: 7.6, unit: '$ / task', period: 'Sep 2026', status: 'bench', src: 'aaSonnet', text: '$7.60' },
  sonnet5_cost: { value: 5.09, unit: '$ / task', period: 'Sep 2026', status: 'bench', src: 'aaSonnet', text: '$5.09' },
  opus55_index: { value: 58, unit: 'index, max effort', period: '22 Sep 2026', status: 'bench', src: 'aaOpus', text: '58' },
  sonnet55_index: { value: 56, unit: 'index, max effort', period: '28 Sep 2026', status: 'bench', src: 'aaSonnet', text: '56' },
};

export const ORDER = ['cover', 'demand', 'retained', 'models', 'statements', 'capacity', 'scenarios', 'filing', 'close'];

// Visible copy, kept short by design (at most 12 words per scene beyond chart labels).
export const SCENES = {
  cover: { kicker: 'Capacity ledger', line: 'Can Claude demand become cash across physical compute?', primary: 'Enter ledger', next: 'demand', sources: ['rainier', 'awsCommit'] },
  demand: { kicker: '01 · Demand', line: 'Four clocks, four bases. None is FY2026 revenue.', primary: 'Trace revenue', next: 'retained', sources: ['reutersFiling', 'bloombergQ2', 'seriesH'] },
  retained: { kicker: '02 · Retained', line: 'Reported revenue is not retained value.', primary: 'Follow retained value', next: 'models', sources: ['reutersFiling', 'axios'] },
  models: { kicker: '03 · Models', line: 'Strong capability. Task cost tells a second story.', primary: 'Inspect task economics', next: 'statements', sources: ['opus', 'sonnet', 'fable', 'aaOpus', 'aaSonnet'] },
  statements: { kicker: '04 · Statements', line: 'Loss is not cash. Adjusted is not GAAP.', primary: 'Look ahead', next: 'capacity', sources: ['reutersFiling', 'bloombergQ2'] },
  capacity: { kicker: '05 · Capacity', line: 'A multi-year floor sits under every path.', primary: 'Test utilization', next: 'scenarios', sources: ['reutersCommit', 'awsCommit', 'rainier'] },
  scenarios: { kicker: '06 · Scenarios', line: 'Three conditional paths. None is a forecast.', primary: 'What must be disclosed?', next: 'filing', sources: ['reutersCommit', 'googleBroadcom', 'aaSonnet'] },
  filing: { kicker: '07 · Filing', line: 'Five disclosures before any investment judgment.', primary: 'Return to the question', next: 'close', sources: ['s1', 'reutersFiling', 'ltbt'] },
  close: { kicker: 'The test', line: 'Demand is visible. Cash conversion is unproven.', primary: 'Restart', next: 'cover', sources: ['reutersFiling', 'reutersCommit'] },
};

export const SCENARIOS = {
  upside: {
    name: 'Upside',
    text: 'If retention and utilization hold and task cost falls, cash conversion improves.',
  },
  base: {
    name: 'Base',
    text: 'If revenue grows but capacity and channel costs absorb the gains, cash stays tight.',
  },
  downside: {
    name: 'Downside',
    text: 'If utilization or pricing lags commitments, the floor outweighs demand.',
  },
};

export const GATES = [
  { id: 'cash', title: 'Cash flow & reconciliation', note: 'GAAP cash flow, capex, and the adjusted-to-GAAP bridge.' },
  { id: 'revenue', title: 'Revenue policy & partner share', note: 'Gross vs net cloud revenue and partner take rates.' },
  { id: 'commit', title: 'Commitments & maturity', note: 'Annual schedule, cancellation and shortfall terms, utilization.' },
  { id: 'conc', title: 'Concentration & retention', note: 'Top-customer share, cohorts, contract length.' },
  { id: 'capital', title: 'Capital & share structure', note: 'Share count, offer terms, voting rights, dilution. None set yet.' },
];
