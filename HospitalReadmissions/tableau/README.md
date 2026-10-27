# Tableau companion

Open `Hospital_Readmissions_Dashboard_Verified.twbx` in Tableau. The package embeds aggregate data only; it does not need the original patient archive. The overview compares validation recall and shows final-test precision and recall with patient-bootstrap intervals. An additional worksheet shows exploratory recall by reported race using the global test review flags. Small-group performance was suppressed in the analysis; displayed subgroup estimates still have uncertainty and do not establish fairness.

The 20% review capacity is illustrative. The model predicts recorded readmission risk, not preventability or the benefit of follow-up. The workbook is a local portfolio artifact, not an online publication.

The accompanying CSVs use percent units (0–100) for the interval chart and fractions (0–1) for recall charts. These are aggregate summaries from the main notebook. Re-running the notebook updates `reports/`; the workbook embeds a snapshot and must be rebuilt or its data updated separately.
