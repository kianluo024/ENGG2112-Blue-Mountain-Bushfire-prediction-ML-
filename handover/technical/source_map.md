# Source and method traceability

Read the experiment runners for orchestration, the shared fitting/metric helpers
for behaviour, configurations for prespecified settings, and JSON for exact
measurements. The evaluated source is frozen; packaging lives under `tools/`.

| Question or claim | Implementation | Settings or evidence | Verification |
| --- | --- | --- | --- |
| What is predicted and which dates are held out? | [data.py](../../bushfire_ml/data.py) `partition_for`, [prepare.py](../../bushfire_ml/prepare.py) `prepare` | [Original protocol](../../config/protocol_v1.json), [partition manifest](../../reports/partition_manifest.json) | [Data guards](../../tests/test_data_guards.py) |
| Which columns may enter a model? | [data.py](../../bushfire_ml/data.py) `model_matrix` | [Final ordered columns](../../reports/final_freeze.json), [feature catalogue](feature_catalog.md) | Answer-column exclusion and current-flag checks |
| Were supplier variables checked independently? | [audit.py](../../bushfire_ml/audit.py) | [Development audit](../../reports/development_audit.json) | Raw weather and causal-history reconstruction; development only |
| Where are scaling and class weights learned? | [models.py](../../bushfire_ml/models.py) `fit_logistic`, `fit_xgboost`, `fit_xgboost_fixed` | [Logistic settings](../../config/baseline_v1.json), [XGBoost settings](../../config/xgboost_v1.json) | [Baseline](../../tests/test_baselines.py), [current-fire](../../tests/test_current_fire.py), [XGBoost](../../tests/test_xgboost.py) checks |
| What does AP mean here? | [evaluation.py](../../bushfire_ml/evaluation.py) `evaluate` | `average_precision_score`; [original evaluation plan](../../config/protocol_v1.json) | AP uses scores before thresholding, not a trapezoidal substitute |
| Did current fire improve the matched logistic comparison? | [current_fire.py](../../bushfire_ml/current_fire.py) | [Comparison](../../reports/current_fire_comparison.json) | Identical rows/settings; one extra audited input |
| Did nonlinear trees help on development dates? | [xgboost_experiment.py](../../bushfire_ml/xgboost_experiment.py) | [First comparison](../../reports/xgboost_comparison.json) | AP stopping explicitly maximises the reported definition |
| Do later outcomes enter earlier fits? | [temporal_stability.py](../../bushfire_ml/temporal_stability.py) `forward_parts`, `fit_forward_window` | [Calendar settings](../../config/temporal_stability_v1.json), [results](../../reports/temporal_stability.json) | [Outer-answer isolation](../../tests/test_temporal_stability.py) |
| Why was calibration not adopted? | [calibration.py](../../bushfire_ml/calibration.py) `fit_sigmoid`, [probability_experiment.py](../../bushfire_ml/probability_experiment.py) `calibration_decision` | [Fixed designs and gate](../../config/probability_v1.json), [results](../../reports/probability_reliability.json) | [Calibration and temporal separation](../../tests/test_probability.py) |
| How were 80% and 90% policies selected? | [calibration.py](../../bushfire_ml/calibration.py) `select_recall_threshold` | [Exact frozen policies](../../reports/final_freeze.json) | Highest feasible calibration-only cutoff; tied scores stay together |
| What was fixed before final access? | [freeze_final.py](../../bushfire_ml/freeze_final.py) `main`, `verify_freeze` | [Committed manifest](../../reports/final_freeze.json), freeze commit `ef45cdf` | Byte hashes, feature order, runtime and committed-source checks |
| Was final evaluation repeated or fitted? | [final_release.py](../../bushfire_ml/final_release.py) `main` | [Release receipt](../../reports/final_release.json) | [One-time access and cached recovery](../../tests/test_final_release.py) |
| Which exact final population was scored? | [final_metrics.py](../../bushfire_ml/final_metrics.py) `validate_population`, `predict_frozen`, `final_results` | [Final rules](../../config/final_evaluation_v1.json), [aggregate](../../reports/final_holdout.json) | Every frozen grid/date pair; no fit calls |
| Where do report numbers come from? | [build_handover.py](../../tools/build_handover.py) | [Claims](../evidence/claims.json), [CSV tables](../tables/README.md) | [Verifier](../../tools/verify_handover.py), [packaging checks](../../tests/test_handover.py) |
| Does the export change the evaluated analysis? | [render_handover_pdf.py](../../tools/render_handover_pdf.py) | [Structured report content](../group_report/report_content.json), [package manifest](../manifest.json) | Rendering consumes aggregates/content only; frozen hashes stay unchanged |

All final numerical statements refer to `reports/final_holdout.json` unless
explicitly labelled development evidence. The claim catalogue records JSON
paths as arrays of keys/indexes, so exact values can be checked without parsing
row-level answers or interpreting rounded prose.
