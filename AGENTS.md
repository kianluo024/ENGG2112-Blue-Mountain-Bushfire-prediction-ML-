# Project working agreements

## Communication and language

- Explain work to Kian in plain Chinese unless asked otherwise.
- All repository-authored filenames, code, comments, documentation, figures and
  Git commit messages must use English.
- Kian understands baselines, error analysis and single-factor comparisons.
  Batch related development work and report at meaningful milestones instead
  of repeating introductory explanations or pausing after every small change.

## Code clarity

- Prefer straightforward functions, descriptive names and an obvious flow from
  data loading to training, prediction and evaluation.
- Share feature selection, preprocessing and metrics rather than copying them
  for each experiment. Keep configuration separate from fitted results.
- Separate training logic from long report-formatting code where practical.
- Avoid unnecessary classes, framework layers and speculative abstractions.
- Comments should explain a non-obvious reason or methodological constraint,
  rather than narrating each line. Keep scientific caveats in the documentation.
- Derive report numbers and figure labels from results instead of duplicating
  measured values as hard-coded claims in executable scripts.
- Preserve meaningful checks for leakage, input alignment and comparable
  experiments when simplifying code. Run checks relevant to changed behaviour.

## Evaluation integrity

- Keep the frozen protocol, data partitions and original baselines intact.
- Development code may parse only training and validation outcomes. Hash checks
  of the sealed holdout bytes are allowed; exploratory test metrics are not.
- Do not change labels, omit difficult dates or move cutoffs to improve scores.
- Compare algorithms with matched inputs and report both persistence and the
  subset without current detections.
- Use development-only, out-of-sample evidence for calibration and thresholds.
  State limitations when the available observations cannot support reliable
  percentages. Do not promise calibrated probabilities from raw model scores.
- Freeze the complete selected pipeline before the final holdout evaluation.
  Report disappointing results honestly and do not tune against that test.

## Git commits

- Group each commit around one coherent, reviewable change.
- Use a clear English subject stating the concrete change, followed by a
  substantive body describing the problem, reason, implementation and checks.
- For experiment commits, record relevant inputs/settings, development results,
  limitations and whether the final holdout remains sealed.
- For refactors, explain the simplification and how behaviour was preserved.
- Do not use vague messages such as "update", "fix stuff" or "final version".
- Prefer a message file with actual newlines for multiline commit bodies.
- Keep raw data, row-level answers/predictions, local models, environments and
  credentials out of Git. Verify the staged file list before committing.
- Do not claim a commit or push happened unless the command succeeded.
