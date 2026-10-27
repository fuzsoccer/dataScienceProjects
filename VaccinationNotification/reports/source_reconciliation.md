# Source reconciliation and final review

## What was checked

The study's primary models were reconciled with the full-text PMC author manuscript identified in `references/SOURCES.md`. Conventional OLS is the correct comparison for the paper's estimates; HC1 intervals and our additional Holm adjustments are separate extensions. Full publisher-layout and all supplementary-table replication are outside this project's scope.

| Comparison | Conventional Python result | Reported manuscript result | Assessment |
|---|---|---|---|
| Pooled high risk vs passive | +2.566 pp; p=.0000145; df=33,957 | +2.6 pp; p<.001; same df | Agrees after rounding |
| Pooled high risk vs active | +1.142 pp; p=.05374; df=34,013 | +1.1 pp; p=.054; same df | Agrees after rounding |
| Active vs passive | +1.424 pp; p=.04708; df=16,986 | +1.4 pp; p=.047; same df | Agrees after rounding |
| Reasons arms minus high risk only | -0.739 pp; p=.24037; df=25,491 | +0.7 pp; p=.240; printed df=25,941 | Magnitude/p agree; reported sign and df differ |
| Framing-by-reasons interaction | +2.031 pp; p=.16191; df=16,991 | +2.0 pp; p=.162; same df | Agrees after rounding |

The source-data subgroup contains 25,493 patients for the reasons-versus-no-reasons model, so a two-parameter model has 25,491 residual degrees of freedom. We retain the computed value and flag the manuscript discrepancy rather than altering the data to match it. The positive reported coefficient has the opposite sign to our explicit reasons-minus-no-reasons coding; available text does not establish whether this is reversed coding or a typographic sign error. It is not described as an exact signed replication.

## Reasons-count estimands are different

The manuscript describes a one-versus-three contrast of about +1.7 pp (p=.096). Our conventional medical-record simple effect, one minus three, is +1.711 pp (p=.09625). Our equal-arm average is three minus one, -0.695 pp, and is explicitly a different estimand. We do not represent our average as a numerical replication of that reported contrast, or infer the authors' intended weighting beyond the available text. The interaction and its uncertainty agree. No superiority or equivalence conclusion is inferred from these null results.

## Message and endpoint checks

The Methods confirm the five messaging roles, the randomized one/three reasons comparison, and the primary September 9-November 5, 2021 outcome window. Explanations were included in letters and SMS, not portal messages. The full verbatim messages are referenced in Supplementary Table 41; that table was not retrievable here. Our labels describe verified message components, not a verbatim reconstruction.

The manuscript identifies the 29-day outcome as a non-preregistered robustness check; it is not the registry's later nine-week secondary vaccination endpoint. The project now labels it accordingly. It also notes that not all Study 2 messages had been sent within that 29-day window, so the shorter window does not capture the entire intervention.

## Final assessment

The main conclusions are supported by the released data and source-model replication. Known manuscript discrepancies, estimand differences, and unavailable full wording are explicit limitations, not hidden matching assumptions. No additional inferential analyses are necessary to present the stated portfolio questions. Rights uncertainty is addressed by excluding third-party source materials from the publication package and linking readers to the source.
