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
Stage 5 has completed the first matched-input XGBoost comparison. The 17-input
variant has validation AP 0.7283 versus persistence AP 0.7056, but exactly the
same binary alerts at the fixed threshold of 0.5. Time-aware stability checks
are now complete: early stopping is isolated from outer checking outcomes,
but sparse early positives prevent two XGBoost fits, and the available windows
do not establish stable improvement over persistence. No final-test evaluation
has been performed.
Stage 6 has checked probability reliability and two recall-target policies.
Sigmoid calibration is not adopted: the longer temporal check worsens, while
the improving recent check has only one calibration day and one assessment day.
Two exact raw-score cutoffs are recorded as provisional research choices;
trusted probability percentages and operational alert thresholds remain
unestablished.
Stage 7 now has an explicit final protocol and dedicated one-time release
runner. Its freeze manifest must be committed before the runner can open final
outcomes. The release receipt and final report record whether evaluation has
actually completed; the presence of the runner alone does not establish that.

## Remaining milestones

| Stage | Deliverable | Status |
| --- | --- | --- |
| 1. Data acceptance and temporal separation | Audited development data and sealed final test | Complete |
| 2. Simple baselines | Prevalence, persistence and core logistic comparison | Complete |
| 3. Error analysis | Error groups, input shifts and observation-quality concerns | Complete |
| 4. Current-fire input comparison | Matched 16-input and 17-input logistic experiments | Complete |
| 5. Main model comparison | Matched-input XGBoost comparison and temporal checks; stability remains unestablished | Complete |
| 6. Probability and alert policy | Reliability checks complete; calibration unadopted; provisional 80%/90% recall policies documented | Complete with limited evidence |
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
- [Lesson 5: understand XGBoost](docs/lesson_05_xgboost.md)
- [Matched-input XGBoost results](reports/xgboost_comparison.md)
- [Lesson 6: temporal stability and honest limits](docs/lesson_06_temporal_stability.md)
- [Temporal diagnostics and forward-window results](reports/temporal_stability.md)
- [Lesson 7: probability reliability and reminder cutoffs](docs/lesson_07_probability_and_thresholds.md)
- [Probability diagnostics and threshold trade-offs](reports/probability_reliability.md)
- [Draft research model and exact cutoffs](reports/draft_probability_policy.json)
- [Lesson 8: freeze and perform one final evaluation](docs/lesson_08_frozen_final_evaluation.md)
- [Final evaluation rules](config/final_evaluation_v1.json)

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
.\.venv\Scripts\python.exe -m bushfire_ml.xgboost_experiment
.\.venv\Scripts\python.exe -m bushfire_ml.temporal_stability
.\.venv\Scripts\python.exe -m bushfire_ml.probability_experiment
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Final release is a separate authorised step. First run
`python -m bushfire_ml.freeze_final`, review and commit the complete freeze,
then run `python -m bushfire_ml.final_release` with the same local environment.
The second command parses the protected final outcomes once. Later calls return
the saved aggregate result without another holdout parse or prediction pass.
Do not change the frozen pipeline after release; further tuning needs new
independent evaluation data. See Lesson 8 for the exact procedure and caveats.

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

Error analysis, the current-fire comparison, temporal checks and the probability/
threshold assessment are complete. The next stage is a complete research pipeline
freeze, including both provisional operating points, followed by one protected
final evaluation. The calibration candidate is not adopted and the cutoffs
do not establish an operational warning service.
Continue to use explicit input whitelists and training-only preprocessing. Report average precision,
precision/recall, probability quality and alert burden. Do not optimise accuracy
alone or select a test period because it gives a preferred score.

The first approved model uses 16 weather and terrain features. The additional
audited same-day `fire_today` flag is approved for the 17-input comparison.
The other rainfall and current-fire additions remain candidate experiments.
The full extended feature set is blocked until its warm-up and unknown
dry-history treatment are documented.

The desired probability output is `100 * P(next-day eligible detection)`.
Development-only checks do not yet establish trustworthy percentages, so the
draft labels its output an experimental model score. Multiplication by 100
does not make an alert reliable. Exact research cutoffs remain on the 0-1 scale;
neither their recall targets nor future calibration improvements are guaranteed.

## References and disclosure

- [scikit-learn: avoiding data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
- [scikit-learn: time-series evaluation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-of-time-series-data)
- [scikit-learn: probability calibration](https://scikit-learn.org/stable/modules/calibration.html)

Source checks, methodological limits and AI-assisted work are recorded in the
audit and lesson notes. Team members must review the work and keep their own
prompt/output and verification records for the course's AI-use appendix.
