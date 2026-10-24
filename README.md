# Blue Mountains Bushfire Prediction

ENGG2112 student research prototype for predicting **next-day eligible VIIRS
active-fire detections** in Blue Mountains National Park grid cells.

The target is fire presence detected by a satellite, including continuing fire.
It is not a confirmed ignition, fire-spread simulation or operational warning.

## Current stage

Stage 1 established data acceptance and a protected temporal holdout. Stage 2
has fitted one prespecified core-feature logistic regression and compared it
with prevalence and persistence on validation data only. The final test remains
sealed; no final-test predictions or scores have been generated.
Stage 3 examines the saved validation errors and source-observation caveats,
without refitting or changing any labels.
Stage 4 adds only the audited same-day fire flag to the logistic inputs, using
the same rows and settings. It improves over the conditions-only model but has
not established a practical improvement over persistence.

## Remaining milestones

| Stage | Deliverable | Status |
| --- | --- | --- |
| 1. Data acceptance and temporal separation | Audited development data and sealed final test | Complete |
| 2. Simple baselines | Prevalence, persistence and core logistic comparison | Complete |
| 3. Error analysis | Error groups, input shifts and observation-quality concerns | Complete |
| 4. Current-fire input comparison | Matched 16-input and 17-input logistic experiments | Complete |
| 5. Main model comparison | XGBoost with matched inputs, limited time-aware development checks, preserved baselines | Pending |
| 6. Probability and alert policy | Development-only reliability checks, justified calibration design and threshold trade-offs | Pending |
| 7. Frozen final evaluation | Evaluate the chosen complete pipeline once on the protected temporal test | Pending |
| 8. ML handover | Clear code, reproducible instructions, figures, limitations and review notes | In progress |

Related development experiments can be run together and discussed at stage
boundaries. Final evaluation follows pipeline freeze. Calibration claims depend
on the amount and quality of independent development evidence.

Code clarity, evaluation integrity and detailed English commit messages are
documented in [the project working agreements](AGENTS.md).

- [Frozen research protocol](config/protocol_v1.json)
- [Development audit](reports/development_audit.md)
- [Partition manifest and hashes](reports/partition_manifest.json)
- [Lesson 1: data, labels and the holdout](docs/lesson_01_data_and_holdout.md)
- [Lesson 2: establish simple baselines](docs/lesson_02_baselines.md)
- [Baseline validation results](reports/baseline_validation.md)
- [Lesson 3: understand the errors](docs/lesson_03_error_analysis.md)
- [Baseline error analysis](reports/baseline_error_analysis.md)
- [Lesson 4: add current fire fairly](docs/lesson_04_current_fire.md)
- [Current-fire comparison](reports/current_fire_comparison.md)

All repository-authored text, code comments and report figures use English.
Raw data, row-level development data and holdout answers stay local.

## Local setup

Python 3.12 was used for verification. From this repository on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m bushfire_ml.prepare --dataset-root "C:\path\to\dataset"
.\.venv\Scripts\python.exe -m bushfire_ml.audit
.\.venv\Scripts\python.exe -m bushfire_ml.baselines
.\.venv\Scripts\python.exe -m bushfire_ml.error_analysis
.\.venv\Scripts\python.exe -m bushfire_ml.current_fire
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

`--dataset-root` must point to the supplied directory containing `model_ready`,
`raw`, `processed` and the supplier metadata. The original dataset is never
modified. The preparation command preserves an existing seal and refuses to
silently replace data or change the protocol after sealing.

## Separation of development and evaluation

| Partition | UTC feature dates | Rows |
| --- | --- | ---: |
| Training | 2019-07-01 to 2019-12-08 | 6,923 |
| Gap | 2019-12-09 to 2019-12-15 | 301 |
| Validation | 2019-12-16 to 2019-12-24 | 387 |
| Gap | 2019-12-25 to 2019-12-31 | 301 |
| Final test, sealed | 2020-01-01 to 2020-06-29 | 7,783 |

Every target date is one UTC day after its feature date. All cells from one
feature date remain together. Cells with less than 10% park coverage are excluded
by a predefined geometric rule, leaving 43 of 52 cells.

The supplied dataset already reserved January onward for testing. This protocol
preserves that boundary and adds seven-day development gaps before any fitting.
It deliberately avoids a random row split and the team's proposed interleaved
weekly split. Seven-day gaps reduce adjacency; they do not establish independence
between long-lived fire events or between locations.

The supplier's README already disclosed aggregate test-label counts, and team
notes describe the full season. This is a protected **retrospective temporal
holdout**, not a double-blind study or a new-season validation. Test-label
summaries and scores are not produced by these development tools.

The holdout is stored separately under ignored `.local_data/holdout/`.
`load_development` rejects any partition except `train` and `validation`.
File hashes detect later changes. This separation prevents accidental reuse;
it is not encryption or an access-control boundary. For stronger independence,
a teammate can retain the test file and run the final frozen evaluation.

## Current findings and next lesson

The initial logistic baseline has validation AP 0.3716, below the constant-score
reference of 0.4134. Persistence has AP 0.7056. At the fixed diagnostic threshold
of 0.5, logistic regression gives 92 true positives, 140 false positives and 68
false negatives. It has not established an improvement on these comparisons.
This does not prove that environmental features lack predictive information.

First interpret these errors and the input differences before adding complexity.
Continue to use explicit input whitelists, training-only preprocessing and a
development-only calibration/threshold procedure. Report average precision,
precision/recall, probability quality and alert burden. Do not optimise accuracy
alone or select a test period because it gives a preferred score.

The first approved model uses 16 weather and terrain features. The additional
audited same-day `fire_today` flag is approved for the 17-input comparison.
The other rainfall and current-fire additions remain candidate experiments.
The full extended feature set is blocked until its warm-up and unknown
dry-history treatment are documented.

Probability output will be `100 * P(next-day eligible detection)`. It needs
out-of-sample calibration checks. A displayed percentage alone does not make
an alert reliable. No percentage predictions are fabricated at this stage.

## References and disclosure

- [scikit-learn: avoiding data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
- [scikit-learn: time-series evaluation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-of-time-series-data)
- [scikit-learn: probability calibration](https://scikit-learn.org/stable/modules/calibration.html)

Source checks, methodological limits and AI-assisted work are recorded in the
audit and lesson notes. Team members must review the work and keep their own
prompt/output and verification records for the course's AI-use appendix.
