# Reproducibility and verification

## Environment

Full analysis/figure verification used Python 3.12.7, JupyterLab 4.2.5, ipykernel 6.28.0 and matplotlib 3.9.2 on Windows. `requirements-notebooks.txt` pins those direct tools; it is not a complete transitive dependency lock or a guarantee that every platform resolves identical dependencies. Standard-library calculations also ran in Python 3.12.10 during initial development. Code declares Python 3.11+ compatibility; the GitHub workflow tests the lightweight suite on 3.11 and 3.12 after publication.

Optional package installation is `python -m pip install -e .`; `python scripts/run.py ...` works directly without installing the package. Package build configuration separately pins setuptools. No other analytical runtime packages are required.

## Source pins and files

`sources.lock.json` records provider revisions and starter-file hashes. It contains no data payloads. The checked-in starter manifest covers three 2022 matches plus Metrica Sample Game 1. Full-tournament acquisition appends further entries locally; original SHA-256 checksums are verified before cached source reuse. Gzip-stored tracking and historical training files are hashed after decompression. Corrupted caches raise errors rather than silently changing data.

Training uses a separate compressed `data/xt_training_2018/` cache and manifest pinned to the same StatsBomb revision. Notebook 06 requires 64 2018 training matches and 64 2022 application matches by default, checks disjoint IDs and temporal ordering, and saves a model/run manifest. Notebook 07 verifies source bytes and reproduces the baseline before comparing alternative grids. Notebook 08 verifies aligned cohorts, source revisions, player IDs, exposure and non-penalty xG across input tables, and saves input hashes plus the selection policy.

The complete fresh-checkout path is notebooks 01 through 08 in order. The command-line `all` task is a smaller acquisition/inspection/tracking demonstration. Full notebooks are not executed by the lightweight GitHub workflow because they download large public inputs and regenerate extensive artifacts.

## Portable notebooks

All checked-in notebooks have cleared outputs, neutral kernel metadata and no machine-specific project fallback. Launch Jupyter from the repository root or `notebooks/`. If necessary set `PROJECT_OVERRIDE` to the complete checkout directory. The marker `src/soccer/cli.py` must exist; a notebook downloaded alone cannot replace the project.

`data/`, `reports/`, virtual environments and caches are ignored. Keep only intentionally reviewed result snapshots under `docs/`. Adding input matches is additive; notebook 02 inspects all downloaded event files while later role/xT analyses explicitly use their tournament catalog/manifests. Use a separate root for a different cohort.

## Verification scope

The core suite covers tracking units, missing-data gaps, period boundaries, speed rejection, output-stride invariance and structural gates. Notebook contract tests compile every code cell, check cleared outputs/unique cell IDs and reject personal project paths. Additional analytical tests exercise the actual notebook xT functions against known values, unsupported zones, invalid endpoints and negative deltas, plus participation reconstruction with stoppage time, halftime substitution and bench discipline.

The original notebook 06 full run was executed on the complete cohorts; notebooks 07 and 08 were independently executed against that saved full-cohort data, and their figures were inspected. Publication cleanup changes project discovery, documentation, output metadata and first-run setup defaults; analytical definitions remain the same. Lightweight tests and analytical-function tests are rerun on the clean copy. They are arithmetic and reproducibility checks, not predictive model validation.

Use the model card and case-study limitations when interpreting results. In particular, a temporally separated fit/application and a high rank correlation do not establish calibrated probabilities, causal player effects or stable recruitment performance.
