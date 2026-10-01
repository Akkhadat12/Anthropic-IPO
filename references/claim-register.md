# Claim register

## C01
Exact claim: Company announced confidential draft S-1 on June1; share count and price unset in announcement
Type: FACT_COMPANY
Sources: SRC01
Unit/period/denominator: 2026-06-01; IPO process
Limits/contrary evidence: No fixed IPO date or final price verified
Permitted visual interpretation: Show submitted draft, never a completed listing or ticker

## C02
Exact claim: FY2025 revenue nearly$4.6B; net loss about$42B including about$34B noncash financing accounting charge per Reuters
Type: FACT_MEDIA_DOCUMENT
Sources: SRC02
Unit/period/denominator: USD; full year2025
Limits/contrary evidence: Original statements/notes not read; not current results or cash burn
Permitted visual interpretation: Keep fiscal period and noncash distinction; do not subtract into cash burn

## C03
Exact claim: Q22026 preliminary revenue>$11.5B vsQ1$4.73B and adjusted operating income positive
Type: FACT_MEDIA_DOCUMENT
Sources: SRC03
Unit/period/denominator: USD; quarterly recognized revenue as reported
Limits/contrary evidence: Preliminary may change; profit amount and reconciliation missing
Permitted visual interpretation: Different labels for Q1/Q2; no inferred cash flow

## C04
Exact claim: Company expected Q3 adjusted operating profit again per FT relayed by Bloomberg
Type: OUTLOOK_MEDIA
Sources: SRC04, SRC12
Unit/period/denominator: Outlook reported2026-09-13 before quarter-end
Limits/contrary evidence: Both stories same FT origin, not two independent verification sources
Permitted visual interpretation: Label forecast; do not show completed second profitable quarter

## C05
Exact claim: At least$518B infrastructure obligations over roughly decade; about80% noncancelable/pay irrespective of usage per Reuters
Type: FACT_MEDIA_DOCUMENT
Sources: SRC05
Unit/period/denominator: USD cumulative multiyear commitments
Limits/contrary evidence: Not annual spend/debt due immediately; full maturity schedule absent
Permitted visual interpretation: Multiyear obligation concept, no uniform annual allocation

## C06
Exact claim: Revenue annualized run-rate>$65B at endJuly2026 perReuters source
Type: FACT_MEDIA_SOURCE
Sources: SRC06
Unit/period/denominator: USD annualized pace; July2026
Limits/contrary evidence: Not full-year actual, recurring contracted revenue, or October current level
Permitted visual interpretation: Keep pace and actual-year metrics separate

## C07
Exact claim: ClaudeCode run-rate>$2.5B; enterprise use over half of Code revenue as company saidFebruary12
Type: FACT_COMPANY
Sources: SRC07
Unit/period/denominator: USD annualized; Code-only denominator; Feb2026
Limits/contrary evidence: Historical not latest product mix; not share of total Anthropic revenue
Permitted visual interpretation: No current revenue pie chart or cross-date ratio

## C08
Exact claim: Two customers accounted for nearly quarter of FY2025 revenue perReuters
Type: FACT_MEDIA_DOCUMENT
Sources: SRC02
Unit/period/denominator: FY2025 revenue concentration
Limits/contrary evidence: No identities established and no current concentration data
Permitted visual interpretation: Label2025; do not project concentration unchanged

## C09
Exact claim: Reported gross margin>80% before partner revenue-share and training costs
Type: FACT_MEDIA_RELAY
Sources: SRC04, SRC12
Unit/period/denominator: Gross-margin metric reportedSep13
Limits/contrary evidence: Not all-in margin or adjusted operating margin; exact denominator/exclusions incomplete
Permitted visual interpretation: No all-cost profit wedge; don't carry exclusions into another metric

## C10
Exact claim: Team has not located public Anthropic S-1/full statements as of cutoff
Type: RESEARCH_LIMIT
Sources: SRC01, SRC05
Unit/period/denominator: 2026-10-01T04:24Z
Limits/contrary evidence: Search non-result is not proof of absence; ReutersSep29 says nonpublic
Permitted visual interpretation: Show evidence boundary, not claim no public financial information

## C11
Exact claim: Current revenue mix/concentration/retention insufficient in reviewed sources
Type: RESEARCH_LIMIT
Sources: SRC02, SRC07
Unit/period/denominator: Current2026 data gap
Limits/contrary evidence: Not proof customer retention poor
Permitted visual interpretation: Unknown marked unknown; no invented distributions

## C12
Exact claim: Reviewed reports do not supply complete adjusted-to-GAAP-to-cash reconciliation
Type: RESEARCH_LIMIT
Sources: SRC02, SRC03, SRC04
Unit/period/denominator: Matching2026 reporting period
Limits/contrary evidence: Do not infer profitability impossible or amounts missing are zero
Permitted visual interpretation: Conceptual bridge only, no numeric waterfall from incompatible periods

## C13
Exact claim: Most xAI capacity commitments described as cancelable with90-day notice perReuters
Type: FACT_MEDIA_DOCUMENT
Sources: SRC05
Unit/period/denominator: Through2029; up to$84.5B
Limits/contrary evidence: Some clauses may vary; Reuters summary not full contract
Permitted visual interpretation: Show flexibility contrast, not every obligation locked

## C14
Exact claim: Operating loss>$8B on Reuters-described basis; compute infrastructure$7.33B, opex$12.65B; cash/equivalents/short-term investments$20.28B
Type: FACT_MEDIA_DOCUMENT
Sources: SRC02
Unit/period/denominator: FY2025 expenses; balance at2025-12-31
Limits/contrary evidence: Not verified current cash; cannot calculate current runway
Permitted visual interpretation: Historical report labels; no net-loss→cash shortcut

## C15
Exact claim: Google$111.1B April2026–July2033; Amazon$110B May2026–April2036; Microsoft$31.4B Nov2026–May2033; Broadcomleases$161.2B
Type: FACT_MEDIA_DOCUMENT
Sources: SRC05
Unit/period/denominator: USD; contract windows
Limits/contrary evidence: Windows not annual payment schedule; component rounding and totals differ
Permitted visual interpretation: Do not add to$518B or infer equal annual payments

## C16
Exact claim: Akamai8K describes$11.6B commitment; seven-year initial terms from service starts, delivery and termination conditions
Type: FACT_PRIMARY_FILING
Sources: SRC08
Unit/period/denominator: AgreementSep18; filingSep24, Item1.01
Limits/contrary evidence: Counterparty filing not Anthropic statements; overlap with Reuters total unresolved
Permitted visual interpretation: No added total or guaranteed cancellation convenience

## C17
Exact claim: SeriesH$65B financing at$965B private post-money valuation; May run-rate>$47B
Type: FACT_COMPANY
Sources: SRC09
Unit/period/denominator: USD; May2026
Limits/contrary evidence: Financing not revenue; private valuation not IPO market cap
Permitted visual interpretation: Keep financing/valuation/operating metrics distinct

## C18
Exact claim: Partner sales accounting may distort direct revenue comparison
Type: FACT_MEDIA_AND_ANALYSIS
Sources: SRC10
Unit/period/denominator: Revenue recognition presentation
Limits/contrary evidence: Policy and current channel share not reconciled
Permitted visual interpretation: No apples-to-apples profitability inference from headline sales

## C19
Exact claim: Company announced>$100B AWS commitment over10years
Type: FACT_COMPANY
Sources: SRC11
Unit/period/denominator: April2026 announcement
Limits/contrary evidence: May overlap Reuters Amazon figure
Permitted visual interpretation: Use corroborative context; never sum twice

## A01
Exact claim: Conditional scenarios link retention, cost per successful task, capacity use and financing need
Type: ANALYSIS_SCENARIO
Sources: SRC02, SRC03, SRC04, SRC05, SRC07
Unit/period/denominator: No forecast values or probabilities
Limits/contrary evidence: Outcomes contingent; no investment recommendation
Permitted visual interpretation: Clearly scenario/schematic rather than measured prediction
