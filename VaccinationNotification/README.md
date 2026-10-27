# Do personalized risk messages increase flu vaccination?

A reproducible Python portfolio analysis of an existing five-arm randomized field study, using 42,481 patients retained in the manuscript analysis population. The original investigators conducted the trial; this project contributes the Python replication, validation, sensitivity checks, and interpretation.

## Read the project

- **Start here:** [self-contained notebook](notebooks/01_study2_eda.ipynb), with all code, saved tables, and two embedded charts.
- **Readable preview:** [HTML notebook](notebooks/01_study2_eda.html), viewable without Jupyter.
- **Portfolio story:** [case study](PORTFOLIO_CASE_STUDY.md) and [short summary/resume bullet](PORTFOLIO_SUMMARY.md).
- **Verification:** [source reconciliation](reports/source_reconciliation.md), [sources](references/SOURCES.md), and [validation record](validation/FINAL_VALIDATION.md).

## Main findings

| Comparison | Difference in vaccination | 95% HC1 interval |
|---|---:|---:|
| Pooled high-risk messages vs no outreach | +2.57 percentage points | +1.42 to +3.71 |
| Pooled high-risk messages vs basic reminder | +1.14 percentage points | -0.01 to +2.30 |
| Three reasons vs one, equal average across the two explanation arms | -0.70 percentage points | -2.12 to +0.73 |

Targeted risk messages outperform no outreach in the analyzed population. Their advantage over a reminder is less certain, and additional explanations show no clear incremental benefit. These findings do not establish equivalence, identify a mechanism, or prove the highest observed arm is best.

## Reproduce

Use Python 3.12. Extract the complete package. For the publication package, obtain the source ZIP from [OSF](https://osf.io/mqbux/) and follow [data setup](data/README.md). The complete working package already includes those inputs. The notebook reads the two CSVs directly and contains every helper function; it never calls the project scripts or reads precomputed reports.

```text
python -m venv .venv
```

Activate the environment (`.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on macOS/Linux), then:

```text
python -m pip install -r requirements-notebook.txt
python src/prepare_data.py --archive /path/to/mqbux-osfstorage-archive.zip
python -m jupyter lab notebooks/01_study2_eda.ipynb
```

Skip `prepare_data.py` when the validated CSVs are already present. Choose **Restart Kernel and Run All** in Jupyter. All 17 code cells passed a fresh Jupyter-kernel execution during final validation. No analysis network access is needed after dependencies and inputs are installed. Fresh notebook exports go to `reports/notebook/`.

For automated notebook execution:

```text
python validation/reproduce_notebook.py
```

The optional scripts provide the same analysis stages from the command line:

```text
python src/analyze.py
python src/extend_analysis.py
python src/analyze_reasons.py
```

## Methods and limits

The notebook includes ID/outcome checks, exclusion and missingness audits, Wilson intervals, baseline standardized differences, source-aligned OLS and HC1 models, risk-stratum adjustment, population sensitivities, logistic checks, and the randomized reasons-count interaction. Holm adjustment is applied within stated families, without global error control across the project. The 29-day endpoint is a non-preregistered robustness outcome, not the registry's later nine-week vaccination endpoint.

The main population excludes some enrolled patients, shared addresses may create dependence or spillovers, and recorded outcomes may be incomplete. Household identifiers and patient-level dates are unavailable. Read [design and robustness](reports/design_and_robustness.md) and [reasons analysis](reports/reasons_analysis.md) for details.

## Provenance, attribution, and sharing

Source: Rosenbaum and colleagues, *Algorithm-assisted personalized risk communication to encourage flu vaccination in the USA: three randomized field trials*, [DOI: 10.1038/s41562-026-02603-4](https://doi.org/10.1038/s41562-026-02603-4); Study 2 [NCT05009251](https://clinicaltrials.gov/study/NCT05009251); [OSF](https://osf.io/mqbux/). We consistently use the manuscript CSV release, not the separate November 2024 registry release. Input hashes identify the exact version.

The publication package omits raw patient-level data and third-party documents/code because the source project's API has no project-level license recorded. Source acquisition remains reproducible. See [third-party notices](THIRD_PARTY_NOTICES.md). The complete working package retains the user-supplied source files for personal analysis.

This is a finished portfolio analysis of the stated questions, with source discrepancies and unavailable verbatim message text documented. It is not a complete replication of every published study analysis. The case study and rendered notebook are published through GitHub Pages from the repository's `docs/` folder. The GoDaddy page is managed separately.
