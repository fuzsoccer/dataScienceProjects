# Validation entry points

Start with FINAL_VALIDATION.md and jupyter_execution.json for the final release. All 17 notebook code cells passed a fresh Jupyter-kernel execution with both charts embedded. Key fresh exports also matched the independently validated script outputs.

To rerun the notebook: python validation/reproduce_notebook.py.

Optional independent R checks, run from the project root:

- Rscript validation/check_models.R: four primary conventional OLS comparisons.
- Rscript validation/check_reasons.R: four interaction coefficients with medical-record/one-reason reference coding.

The saved r_model_validation.csv and r_reasons_validation.csv matched Python estimates, conventional standard errors, and p-values within numerical tolerance. R is not required to run the Python notebook.

Earlier notebook_execution.txt and self_contained_notebook_execution.txt in the private working package are historical intermediate checks; FINAL_VALIDATION.md supersedes their execution limitations.
