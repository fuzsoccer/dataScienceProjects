# Final validation

Completed October 27, 2026, using Python 3.12.7.

- All 17 notebook code cells executed sequentially in a fresh **Jupyter kernel**, using `validation/reproduce_notebook.py`. No cell errors; two PNG charts embedded. See `jupyter_execution.json`.
- Notebook analysis definitions are inline. No `runpy`, project-script imports, or reading of precomputed report tables is used to derive results.
- Input hashes were checked by `src/prepare_data.py` against the supplied OSF archive before notebook execution.
- ID uniqueness, inclusion-population agreement, binary outcomes, matched assignments/risk/outcomes, and timing-outcome consistency were asserted in the notebook.
- Rates, main OLS/HC1 models, risk-adjusted models, reasons contrasts, and logistic models matched the earlier validated outputs within numerical tolerance.
- Conventional estimates, standard errors, and p-values for the four source comparisons and the four interaction coefficients independently matched R. The optional R validation scripts and saved reference CSVs are included.
- Main estimates were reconciled with the PMC author manuscript. Known sign, degrees-of-freedom, and estimand discrepancies are recorded in `reports/source_reconciliation.md`.
- Notebook schema, sequential execution counts, embedded output charts, and package contents were checked. The HTML preview contains the full code and saved results without requiring Jupyter.

Reproduce with `python validation/reproduce_notebook.py` after installing `requirements-notebook.txt` and obtaining the two validated CSV inputs. The separate script implementations remain optional.

Scope limits are explicit: no all-results replication, no unavailable verbatim-message reconstruction, no global family-wise adjustment across the entire project, and no claim that a null result establishes equivalence. The publication package excludes third-party source materials and patient-level inputs.
