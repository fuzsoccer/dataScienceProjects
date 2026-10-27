# Interview talking points

## One-minute explanation

I built a discharge-time readmission prediction case study using historical public hospital data involving patients with diabetes. I restricted the cohort to discharge home and split by patient, so a person's encounters could not leak across training and evaluation groups. I compared a prevalence baseline, logistic regression and one random forest. The forest's validation improvement was below a predefined practical requirement, so I retained logistic regression before evaluating the reserved test set.

On 14,653 test encounters, the selected model achieved ROC AUC 0.657. An illustrative policy of reviewing the highest-scoring 20% captured 38.9% of recorded readmissions with 18.9% precision. I used patient-level bootstrap sampling for uncertainty and reported missed readmissions and false alarms. The work demonstrates model evaluation and decision trade-offs; it does not establish that follow-up would prevent readmissions.

## Questions to prepare for

**Why not choose the forest if its scores were higher?** Its validation recall improved by only 0.87 percentage points, below our 2-point requirement. The simpler model was preferred under that rule. This does not prove that logistic regression is universally superior or that the score difference is statistically significant.

**Why split by patient?** A patient may have several encounters. Row-level splitting could place the same person in training and test, making evaluation less representative of new-patient performance.

**Why not accuracy?** About one in ten eligible encounters had a recorded <30-day readmission. Predicting the majority outcome would look accurate while identifying no readmissions. Average precision, ranking, calibration and capacity metrics are more informative here.

**What does precision mean?** Of encounters selected for review, 18.9% had a recorded readmission. It does not mean the model was correct on only that percentage of all encounters.

**What does recall mean?** The review list contained 38.9% of all recorded readmissions in test. Most were still missed at the chosen review quota.

**Why is test performance higher than validation?** They contain different patients and different mixes of encounters. We report the observed results and uncertainty without tuning to the test result.

**What do the confidence intervals include?** Approximate variation from sampling test patients and retaining their encounters, conditional on this fitted model. They do not include uncertainty from retraining, model selection, new time periods or new hospitals.

**Is this a clinical readmission quality measure?** No. The source label is less than 30 days, not a reconstructed inclusive endpoint. We cannot distinguish planned readmissions or establish complete follow-up.

**What would be needed in practice?** Recent representative data, verified predictor timing, temporal and hospital validation, operational capacity and costs, subgroup uncertainty, and a prospective evaluation of any follow-up intervention.
