# Study 2: model replication, balance, and sensitivity

## Question and estimand

For enrolled patients retained in the manuscript analysis population, how does the recorded probability of primary-window influenza vaccination differ between assigned messaging groups? Report absolute differences in percentage points. The pooled high-risk contrast combines high risk only, medical records + reasons, and algorithm + reasons, weighted by their observed sample sizes. It does not isolate algorithm messaging.

This is a retrospective analysis plan written after EDA. These estimates are conditional on the supplied population exclusions. Outcome ascertainment and potential interference still limit causal interpretation.

## Verified design

The [registered plan](https://cdn.clinicaltrials.gov/large-docs/51/NCT05009251/SAP_000.pdf), dated November 10, 2021, confirms individual randomization within risk strata and randomized reasons counts within risk/message strata. It sets the primary cutoff to November 5, 2021 after outreach delays. Its four confirmatory comparisons use unadjusted tests; our Holm results are an added conservative analysis. The plan was dated after outreach but states outcomes had not been extracted or analyzed. See `references/registered_analysis_plan.pdf`, PDF pages 2-5. Full message wording remains unverified.

The supplied web appendix (PDF pages 17-20) confirms observational modality comparisons and operational SMS delays, and its SMS subgroup counts match the released data. It is additional analysis material, rather than the complete protocol. See `references/web_appendix.pdf`.

## Source-aligned comparisons

The supplied R script's analyses 1a, 1b, 2, and 3 were translated into binary-predictor linear probability models. Conventional OLS estimates, standard errors, and p-values were independently checked against R for all four comparisons and matched within numerical tolerance. This verifies the translation of these models, not every analysis or table in the original research.

The extension also supplies HC1 heteroskedasticity-robust standard errors with t-based intervals. The source explicitly includes HC1 robustness checks for 1a, 1b, and 3; applying HC1 to comparison 2 is an extension.

| Comparison | Difference (pp) | HC1 95% CI (pp) | Unadjusted p | Holm p |
|---|---:|---|---:|---:|
| Pooled high risk vs active control | +1.14 | -0.01 to +2.30 | .0527 | .1412 |
| Pooled high risk vs passive control | +2.57 | +1.42 to +3.71 | .0000119 | .0000476 |
| Reasons arms vs high risk only | -0.74 | -1.98 to +0.50 | .2412 | .2412 |
| Active vs passive control | +1.42 | +0.02 to +2.83 | .0471 | .1412 |

Holm adjustment here covers these four comparisons within each population/endpoint. It is a different family from the initial seven-comparison report. Intervals are individual 95% intervals, not simultaneous intervals. No global error control is claimed across all endpoints, sensitivity populations, and earlier analyses.

Adding the risk-stratum indicator gives +1.15 pp versus active control (HC1 95% CI -0.01 to +2.30) and +2.57 pp versus passive control (+1.42 to +3.72), essentially unchanged. These adjusted coefficients come from a common-effect linear model, not from a treatment-by-risk interaction model. Full outputs are in `risk_adjusted_models.csv`.

## Baseline balance

For each categorical level, a binary indicator was created and the difference in proportions standardized by the square root of the average of the two Bernoulli variances. All ten arm pairs were evaluated. These are descriptive checks, without balance-test p-values.

Maximum absolute standardized differences in the enrolled sample: sex .0242, race .0373, ethnicity .0176, underlying risk .0010, and original outreach eligibility .0365. In the analysis sample the largest value was .0422 for a race category; maxima for age bin, sex, ethnicity, risk, PCP indicator, and shared-address flag were all below .034.

The observed characteristics show small imbalances by this metric. This does not prove randomization or absence of unmeasured imbalance. Age, PCP, and shared-address indicators are unavailable in the full-enrollment file, so their checks concern the selected analysis population. Message delivery and number of reasons are not included as baseline covariates.

## Sensitivity to population selection

| Population | N | High risk vs active (pp) | High risk vs passive (pp) |
|---|---:|---:|---:|
| Manuscript analysis | 42,481 | +1.14 | +2.57 |
| Analysis, no shared address | 35,001 | +1.51 | +2.78 |
| Enrolled except contraindications | 44,498 | +1.22 | +2.54 |
| All enrolled records | 45,061 | +1.17 | +2.48 |

The second and third rows implement sensitivity populations used in the source R script; the all-enrolled row is an additional check. The source labels its enrolled-except-contraindications sample as intent to treat. We use its literal population definition because 103 randomized patients are absent from enrollment and contraindications remain excluded. The all-enrolled sample also omits those 103 and is not full randomized-population ITT.

Pooled high risk versus passive control remains positive, with HC1 intervals excluding zero in every population. The active-control comparisons are smaller, and none passes the four-comparison Holm adjustment in its family. Reasons arms versus high risk only do not show a clear improvement in any population checked.

Restoring excluded patients also restores early vaccinations, deaths, and other exclusions, changing the target population and interpretation. This is a robustness description, not a cure for post-randomization selection. Removing shared-address patients changes the population and does not provide household-clustered standard errors; cluster IDs are not released.

## Non-preregistered 29-day robustness endpoint

In the analysis population, pooled high-risk messaging versus passive control is +3.01 pp (HC1 95% CI +2.07 to +3.95), whereas versus active control it is +0.20 pp (-0.78 to +1.18). Active versus passive is +2.81 pp (+1.64 to +3.98). The reasons contrast is -1.02 pp (-2.07 to +0.03). This is consistent with early uptake differences between any outreach and passive control, but does not identify a mechanism or establish longer-term equivalence.

## Reproducibility and remaining checks

Run `python src/extend_analysis.py` after installing the requirements. Outputs include detailed pairwise balance, conventional and HC1 model results, exclusion tables, and an extension manifest. Every model's treatment coefficient is asserted to match its direct difference in outcome means.

The models use individual-patient independence; the additional adjusted models include risk strata. The released CSV contains no patient-level vaccination dates, so its endpoint coding cannot be independently reconstructed. Full message text, allocation implementation, publication/registry reconciliation, and licensing remain to be checked. Cluster identifiers are unavailable. No inference of equivalence or mechanism is justified by these results.

Final review: the 29-day outcome is a non-preregistered robustness check, distinct from the registered later vaccination endpoint. Source-message and published-number reconciliation is in `source_reconciliation.md`. Raw source files and PDFs are retained only in the complete working package; obtain them upstream when using the publication package.
