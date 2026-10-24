# Delivery tools

These scripts package and verify the completed research. They do not alter
frozen source or read `.local_data/` unless the verifier's explicit hash-only
private-artifact option is selected.

| Script | Inputs | Outputs |
| --- | --- | --- |
| [build_handover.py](build_handover.py) | Explicitly listed aggregate JSON and configurations | Shared report content, Markdown/LaTeX, CSV tables, figures, feature/claim indexes and manifest |
| [render_handover_pdf.py](render_handover_pdf.py) | Structured report content and exported figures | Reviewed ML contribution PDF; refreshes package hashes |
| [verify_handover.py](verify_handover.py) | Frozen hashes, final receipt, aggregate JSON, package files and links | Public integrity/claim checks; optional private byte-hash verification |

See the [runbook](../handover/technical/runbook.md). The source-of-truth numbers
remain in `reports/`; exporting them is not another final evaluation.
