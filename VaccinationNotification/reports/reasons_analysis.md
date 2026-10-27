# Does giving more personalized reasons improve vaccination uptake?

This extension examines the 16,995 analyzed patients assigned to the medical-record or algorithm messages. Within these arms, patients were randomized to one or three reasons. The other three messaging arms are not part of this factorial comparison. The randomization was verified in the registered plan during the previous milestone; reasons count is not an independently randomized factor across all five arms.

## Observed outcomes

| Message framing | Reasons | N | Vaccinated | Rate |
|---|---:|---:|---:|---:|
| Medical records | 1 | 4,318 | 1,508 | 34.92% |
| Medical records | 3 | 4,152 | 1,379 | 33.21% |
| Algorithm | 1 | 4,326 | 1,446 | 33.43% |
| Algorithm | 3 | 4,199 | 1,417 | 33.75% |

## Model and contrasts

The source interaction model is a linear probability model: vaccination ~ algorithm framing + three reasons + their interaction. Explicit reference categories are medical-record framing and one reason. Conventional estimates reproduce the supplied R formula; Python and independently run R agree for all four coefficients, standard errors, and p-values. HC1 robust inference is an extension.

The interaction is a difference in differences: (three minus one in the algorithm arm) minus (three minus one in the medical-record arm). A positive interaction does not by itself establish a benefit from three reasons in either arm.

| Contrast | Difference (pp) | HC1 95% CI (pp) | Raw p | Holm p |
|---|---:|---|---:|---:|
| Three vs one: medical records | -1.71 | -3.73 to +0.31 | .0968 | .3870 |
| Three vs one: algorithm | +0.32 | -1.69 to +2.33 | .7543 | .7543 |
| Interaction: algorithm minus medical records | +2.03 | -0.81 to +4.88 | .1619 | .4856 |
| Three vs one: equal-arm average | -0.70 | -2.12 to +0.73 | .3383 | .6765 |

The average assigns equal weight to the two messaging arms. Its uncertainty includes covariance between model terms. It is not a raw pooled comparison with sample-dependent weights. The four related contrasts are treated as one exploratory Holm family per population and endpoint. Individual confidence intervals are unadjusted. This does not control error across the entire portfolio's analyses.

## Robustness and selection

Risk adjustment adds separate risk-stratum intercepts within each messaging arm. It assumes each arm's reasons effect is common across the two risk strata. The equal-arm average becomes -0.73 pp (-2.15 to +0.69); the interaction becomes +2.01 pp (-0.84 to +4.85).

The average remains negative with intervals crossing zero when removing shared-address patients (-1.01 pp), including enrolled patients except contraindications (-0.49 pp), or including all enrolled records (-0.53 pp). In the four-week analysis the average is -0.26 pp (-1.46 to +0.93). All interaction intervals in these checks also cross zero. These are sensitivity descriptions, not independent replications.

Enrolled cells were nearly equal: medical records had 4,505 one-reason and 4,498 three-reason assignments; algorithm had 4,511 and 4,506. Analysis exclusions were higher for three-reason assignments: 7.69% versus 4.15% in medical records, and 6.81% versus 4.10% in algorithm. The full exclusion breakdown by reason, message, reasons count, and risk stratum is exported. Because exclusions can affect the randomized comparison, sensitivity results matter; they do not restore all 45,164 randomized patients or establish absence of selection bias.

## Logistic sensitivity for the earlier main comparisons

For the four earlier binary group comparisons, unadjusted logistic models give odds ratios of 1.053 (high risk vs active), 1.124 (high risk vs passive), 0.968 (reasons arms vs high risk only), and 1.067 (active vs passive). With Holm adjustment within those four comparisons, only high risk versus passive meets the .05 threshold. This agrees with the robust linear model interpretation. Odds ratios are not relative vaccination risks, and changing the model on the same data is not new independent evidence. These logistic checks concern the main group comparisons, not a logistic reasons-interaction analysis.

## Interpretation

There is no clear evidence here that providing three reasons improves vaccination uptake, or that its effect differs by algorithm versus medical-record framing. These results do not establish equivalence, rule out all practically meaningful differences, or show that explanations are inherently ineffective. The clearest result in the broader analysis remains the pooled high-risk messages versus passive control comparison.

Rebuild with `python src/analyze_reasons.py`. See `reasons_contrasts.csv`, `reasons_cell_rates.csv`, `reasons_exclusion_audit.csv`, `logistic_sensitivity.csv`, and `reasons_effects.png`. Optional independent validation: `Rscript validation/check_reasons.R` from the project root.

Final review: the 29-day outcome is a non-preregistered robustness check, distinct from the registered later vaccination endpoint. Source-message and published-number reconciliation is in `source_reconciliation.md`. Raw source files and PDFs are retained only in the complete working package; obtain them upstream when using the publication package.
