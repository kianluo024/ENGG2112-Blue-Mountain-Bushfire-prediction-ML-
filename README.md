# Blue Mountains Bushfire Prediction

ENGG2112 research prototype for **next-day eligible VIIRS active-fire detections**
in Blue Mountains National Park grid cells. Kian's ML work is complete and
packaged for technical review and integration into the group report.

The target includes continuing fire. It is not confirmed ignition, fire spread
or severity. The final evaluation does **not** establish reliable warning
probabilities or an operational alert system.

## Start here

| Reader | Entry point |
| --- | --- |
| Group members and report editor | [ML handover](handover/README.md) |
| Report writer | [English ML contribution](handover/group_report/ml_sections.md), [PDF](handover/group_report/ml_contribution.pdf), [integration guide](handover/group_report/integration_guide.md) |
| Code reviewer | [Source and method map](handover/technical/source_map.md), [code index](bushfire_ml/README.md) |
| Reproduction reviewer | [Runbook](handover/technical/runbook.md), [evidence manifest](handover/manifest.json) |
| Results reviewer | [Final report](reports/final_holdout.md), [final interpretation](docs/final_findings.md) |

## Final result

The complete pipeline was frozen in commit `ef45cdf` before a single authorised
temporal evaluation. The feature dates were 1 January to 29 June 2020:
7,783 cell-days, 43 cells, 181 dates and 49 positive next-day targets.

| Frozen policy | True positives | False positives | False negatives | Recall | Precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| 80% development selection-recall target | 16 | 39 | 33 | 32.7% | 29.1% |
| 90% development selection-recall target | 34 | 2,434 | 15 | 69.4% | 1.4% |
| Persistence | 16 | 39 | 33 | 32.7% | 29.1% |

The names describe development selection constraints, not achieved final
recall. XGBoost 17 AP was 0.1062, persistence AP 0.0992 and the prespecified
logistic 17 comparison AP 0.2113. No model, feature, calibration setting or
cutoff was changed after release. Counts are cell-days, not independent fires.

The raw scores are not validated probabilities. A no-alert reference achieves
99.37% accuracy while missing every positive target. See the
[complete aggregate results](reports/final_holdout.json),
[committed freeze](reports/final_freeze.json) and
[one-time release receipt](reports/final_release.json).

## Repository layout

| Directory | Purpose |
| --- | --- |
| [bushfire_ml/](bushfire_ml/README.md) | Frozen data guards, fitting, evaluation and experiment runners |
| [config/](config/README.md) | Versioned protocol and experiment settings |
| [reports/](reports/README.md) | Original chronological evidence, aggregate JSON, reports and figures |
| [docs/](docs/README.md) | Teaching notes and development decisions |
| [tests/](tests/README.md) | Synthetic/unit checks for leakage, chronology and release integrity |
| [handover/](handover/README.md) | Classified technical handover and report-ready English material |
| [tools/](tools/README.md) | Aggregate-only packaging and verification; no model fitting or raw-data access |
| `.local_data/` | Ignored private data, row-level predictions and local model snapshots |

Frozen source files and historical reports remain in their original paths.
The handover adds navigation and exports without rewriting the evaluation
history. All repository-authored content and commit messages use English.

## Review without private data

Use Python 3.12 and the recorded versions in [requirements.txt](requirements.txt).
On Windows, replace `python` below with `.\.venv\Scripts\python.exe` when using
the existing local environment.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe tools/verify_handover.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m bushfire_ml.final_release
```

The last command returns the **published cached result**. It does not reopen
the holdout or predict again, including in a clone without `.local_data/`.
Packaging can also be regenerated from aggregate reports; see the runbook.
Optional PDF-export dependencies are separate from the frozen ML environment.

## Evaluation boundaries

The supplied future-test boundary was preserved. Seven-day gaps separate
development partitions; the first two feature days are excluded from fitting
because of rainfall warm-up. All cells from a date stay together. The original
[protocol](config/protocol_v1.json) and [partition manifest](reports/partition_manifest.json)
record the exact rules. The final model uses 17 reviewed inputs, as recorded
in the later frozen manifest; the original protocol is preserved as history.

This is a protected **retrospective temporal holdout**, with earlier aggregate
disclosures and dependent ongoing events, not independent-season or double-blind
validation. Retrospective input publication latency is not reproduced. The
initial seal records preparation-time status; the release receipt records the
later final evaluation. Do not delete that receipt, retune on this exposed test,
or present a repeat as a new blind result. Further modelling needs new independent
evaluation data.

## Completion and remaining group work

ML data acceptance, baselines, error analysis, matched model comparisons,
temporal checks, probability/threshold assessment, final freeze/evaluation and
handover are complete. The ML contribution does not claim that the entire group
submission is complete. The editor still needs the confirmed team details,
study-area/data documentation, literature discussion, agreed recommendations
and member verification. The integration guide maps these to the supplied rubric.

The supplied course material requires a PDF report with a public code link,
at most ten body pages, and an AI-use appendix for substantive assistance.
Keep prompts/outputs and record each member's actual verification. The
[working agreements](AGENTS.md) and [AI disclosure record](handover/group_report/ai_use_appendix.md)
make these responsibilities explicit.
