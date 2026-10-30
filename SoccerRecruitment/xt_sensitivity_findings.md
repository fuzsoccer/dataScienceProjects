# Attacking-value case study: sensitivity and interpretation

<img src="assets/statsbomb-logo.png" alt="StatsBomb — event data source" width="240">

The 12×8 historical baseline was reproduced from verified source events. Training uses 64 matches from 2018; application uses 64 matches from 2022. Values describe selected successful passing and carrying contributions, not overall player impact.

## Specification sensitivity

| Grid | Minimum minutes | Eligible players | Spearman vs baseline | Top-10 overlap |
|---|---:|---:|---:|---:|
| 8x6 | 180 | 351 | 0.800 | 5 |
| 12x8 | 180 | 351 | 1.000 | 10 |
| 16x12 | 180 | 351 | 0.865 | 4 |
| 8x6 | 300 | 196 | 0.836 | 6 |
| 12x8 | 300 | 196 | 1.000 | 10 |
| 16x12 | 300 | 196 | 0.894 | 6 |
| 8x6 | 450 | 54 | 0.804 | 8 |
| 12x8 | 450 | 54 | 1.000 | 10 |
| 16x12 | 450 | 54 | 0.854 | 8 |

At the 300-minute threshold, alternative grids share 6/10 (8x6), 6/10 (16x12) top-10 players with the baseline. Exact shortlist membership is sensitive to grid resolution; a high broad rank correlation does not establish a definitive top ten.

## Illustrative players

These players were chosen retrospectively from the top baseline totals. Their differences are not causal effects or established ability differences.

### Kylian Mbappé Lottin (France)

Across 7 appearances and 691.2 elapsed minutes: movement xT 0.814, passing 0.292, carrying 0.521, and 0.106 per 90. There were 6 positive and 1 negative match totals. The largest match accounted for 22.0% of positive movement xT.

Observed-appearance resampling range (2.5th–97.5th percentiles, fixed model): 0.043–0.160 per 90. This is descriptive sensitivity, not a calibrated confidence interval. The player qualified in 9 of 9 specification/eligibility combinations.

### Lionel Andrés Messi Cuccittini (Argentina)

Across 7 appearances and 791.2 elapsed minutes: movement xT 0.811, passing 0.230, carrying 0.581, and 0.092 per 90. There were 7 positive and 0 negative match totals. The largest match accounted for 25.1% of positive movement xT.

Observed-appearance resampling range (2.5th–97.5th percentiles, fixed model): 0.056–0.137 per 90. This is descriptive sensitivity, not a calibrated confidence interval. The player qualified in 9 of 9 specification/eligibility combinations.

### Raphael Dias Belloli (Brazil)

Across 5 appearances and 338.7 elapsed minutes: movement xT 0.778, passing 0.598, carrying 0.180, and 0.207 per 90. There were 5 positive and 0 negative match totals. The largest match accounted for 31.9% of positive movement xT.

Observed-appearance resampling range (2.5th–97.5th percentiles, fixed model): 0.116–0.379 per 90. This is descriptive sensitivity, not a calibrated confidence interval. The player qualified in 6 of 9 specification/eligibility combinations.

## Limits and next evidence

Grid sensitivity does not test predictive calibration. Match resampling holds the model fixed and ignores many dependencies and selection effects. No inference of overall impact, transfer value or superiority follows from a narrow rank gap. Review the top action IDs and pitch maps with video/context, check role-specific peers, and use a separate untouched cohort if exploratory findings guide model changes.

Data source: StatsBomb Open Data. Follow the supplied source terms and logo requirements before public distribution. Model inspiration: Karun Singh's Expected Threat and socceraction; the explicit variant and attribution scope are documented in notebook 06.
