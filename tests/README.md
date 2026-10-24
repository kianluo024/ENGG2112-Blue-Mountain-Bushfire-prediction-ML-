# Verification index

The checks use synthetic data or configuration/fixture files. They do not
need private raw data and do not repeat the final holdout evaluation.

| Test module | Consequential behaviour checked |
| --- | --- |
| [test_data_guards.py](test_data_guards.py) | Chronological boundaries, excluded predictors and sealed-file tampering |
| [test_baselines.py](test_baselines.py) | Metrics, denominators and training-only preprocessing |
| [test_current_fire.py](test_current_fire.py) | Exactly one audited additional input and matched settings |
| [test_xgboost.py](test_xgboost.py) | Training-only class weights, AP maximisation and native model persistence |
| [test_temporal_stability.py](test_temporal_stability.py) | Calendar gaps, missing classes, fixed-tree refitting and outer-answer isolation |
| [test_probability.py](test_probability.py) | Natural-prevalence calibration, tied cutoffs and assessment-answer isolation |
| [test_final_release.py](test_final_release.py) | Committed freeze, one-time access, cached recovery and exact cutoff replay |
| [test_handover.py](test_handover.py) | Package integrity, aggregate provenance and absence of raw-data dependencies |

Run `python -m unittest discover -s tests -v`. The original 48 checks passed
before final release. New packaging checks are additional; they do not alter
the frozen original test files or convert the final test back into development
data.
