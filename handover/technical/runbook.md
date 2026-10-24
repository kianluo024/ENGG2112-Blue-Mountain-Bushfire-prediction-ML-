# Review and reproduction runbook

## Public review

The public repository includes the frozen source, aggregate evidence, report
text, figures and release receipt. It excludes private datasets and fitted
model files. No private files are needed for the following review path.

```powershell
git clone https://github.com/kianluo024/ENGG2112-Blue-Mountain-Bushfire-prediction-ML-.git
cd ENGG2112-Blue-Mountain-Bushfire-prediction-ML-
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe tools/verify_handover.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m bushfire_ml.final_release
```

The last command returns cached aggregates. A published completed receipt
prevents a fresh release even without ignored local state. Do not remove the
receipt to force another test. Unit tests use synthetic fixtures and do not
read the private holdout.

The released aggregate has a file-specific Git attribute preserving its exact
recorded bytes. Do not normalise its line endings or rewrite it with a JSON
formatter: the existing release receipt checks its byte hash. See the
[verification record](../evidence/verification.md) for the storage correction.

## Regenerate report exports

```powershell
.\.venv\Scripts\python.exe tools/build_handover.py
.\.venv\Scripts\python.exe -m pip install -r requirements-handover.txt
.\.venv\Scripts\python.exe tools/render_handover_pdf.py
.\.venv\Scripts\python.exe tools/verify_handover.py
```

The first command reads only the explicitly listed aggregate JSON files. It
exports Markdown, LaTeX, tables, figures, a feature catalogue and claim paths.
The second installs optional PDF tools; it does not change the frozen ML
requirements file. The PDF renderer consumes the shared structured report
content, so its values cannot silently diverge from the text/table exports.
Rebuilds are presentation operations, not another evaluation. Review the PDF
visually after layout changes. Do not edit generated measured values by hand.

## Check private artifacts when available

```powershell
.\.venv\Scripts\python.exe tools/verify_handover.py --local-artifacts
```

This additionally hashes the existing private model snapshots, sealed data
bytes and saved final prediction file. It does not parse the test CSV or
perform prediction. Keep the private paths recorded in the frozen manifest;
the exact models and class-weighted/scaled preprocessing are part of the
evaluated pipeline. Reconstructing similar models is not a byte-identical
replay and cannot create a fresh blind claim.

## Development history

The original teaching/experiment commands remain documented in the lessons
and source map. They are not the default current review path: rerunning them
in the delivered working tree would overwrite historical development outputs.
If an experiment needs replication, use a separate checkout of its original
commit, the supplier dataset and its recorded settings. Label any replication
as such; the exposed final period must not be reused for tuning or another
claim of independent evaluation.

The record includes the following checkpoints:

| Commit | Milestone |
| --- | --- |
| `aa0fdf8` | Acceptance, protected split, baselines and first reviewed current-fire comparison |
| `4f02dbe` | Separate shared fitting/metrics from reporting |
| `8abfd9e` | Matched shallow XGBoost comparison |
| `96fc3f9` | Past-only temporal checks |
| `ad81139` | Probability checks and both research cutoffs |
| `ef45cdf` | Freeze committed before final outcome access |
| `39d1230` | Single final result and interpretation |

## Files not distributed publicly

Raw/archive/GIS files, sanitised row-level development tables, final labels,
row-level predictions, model binaries, environments, course screenshots,
original student-identifying documents and credentials are not part of the
public package. Dataset acquisition/licensing and team author details need
their owners' confirmation. The course template's sample claims are examples,
not evidence about this project.
