# ML handover

This package delivers Kian's completed ML work and English material for the
group report. It preserves the frozen experiment and its negative findings.
It is not a completed whole-group submission or an operational warning service.

## Choose an entry point

| Need | File |
| --- | --- |
| Read the ML report contribution | [Markdown](group_report/ml_sections.md), [four-page PDF](group_report/ml_contribution.pdf) |
| Insert material into the supplied LaTeX report | [Integration guide](group_report/integration_guide.md), [methods](group_report/ml_methods.tex), [findings](group_report/ml_findings.tex), [recommendations](group_report/ml_recommendations.tex) |
| Explain changes from the proposal | [Plan versus implementation](group_report/proposal_changes.md) |
| Complete course disclosure and member review | [AI-use appendix](group_report/ai_use_appendix.md) |
| Trace a method or implementation choice | [Source map](technical/source_map.md), [feature catalogue](technical/feature_catalog.md) |
| Verify or regenerate the package | [Runbook](technical/runbook.md), [manifest](manifest.json) |
| Reuse a table or figure | [Aggregate CSV tables](tables/README.md), [report figures](group_report/figures/README.md) |
| Check a numerical claim | [Machine-readable claim catalogue](evidence/claims.json) |
| Inspect completed delivery checks | [Verification record](evidence/verification.md) |

The report text, tables and figures are derived from the existing aggregate
results. Packaging does not read raw data, predict again, fit models or change
thresholds. Original reports, source files and frozen configurations stay in
their original paths so their hashes and chronology remain checkable.

## Delivery status

The ML implementation, tests, evidence, frozen final evaluation and handover
are delivered. The group still needs its verified data/map provenance,
literature synthesis, author details and member sign-off. Suggested ownership
is based on the supplied team specification; no person's review is claimed
to have happened. See the integration guide before assembling the final PDF.

Private raw data, row-level predictions, model binaries and environments remain
outside Git. Public review and cached final-result display work without them.
If private snapshots are shared separately, their hashes must match the frozen
manifest. The final test has already been exposed and is not a tuning set.
