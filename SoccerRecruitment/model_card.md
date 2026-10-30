# Model card: selected open-play movement xT

| Item | Specification |
|---|---|
| Intended use | Retrospective attribution of attacking movement value and illustration of a scouting-review workflow |
| Training | 64 men's 2018 World Cup matches; verified run retained 65,420 selected actions and 62 goals |
| Application | 64 men's 2022 World Cup matches; 45,546 eligible successful movements |
| Primary grid | 12×8 zones on the standardized StatsBomb 120×80 coordinate system |
| Inputs | Pass attempts, observed carries and non-penalty shots in Regular Play/From Counter possessions |
| Location values | Iterative goal-based Markov baseline; failed passes and missed shots terminate at zero |
| Action attribution | Signed destination value minus origin value for successful selected movements only |
| Exposure | Actual elapsed participation, including stoppage/temporary absences, excluding breaks/shootouts |
| Sensitivity | 8×6, 12×8, 16×12 training grids; 180/300/450-minute eligibility; observed-match resampling |
| Uncertainty | Sparse-zone/coverage diagnostics and exploratory sensitivity; no validated probability or causal uncertainty guarantee |

No 2022 events enter the fit. The 2022 application subsequently supports exploratory model/shortlist sensitivity and retrospective illustrative selection. Any future changes informed by those findings need another untouched evaluation cohort. Match resampling holds the model fixed and does not account for all dependence, selection, opponent or model uncertainty.

Every baseline application movement had observed training-zone coverage; none triggered the illustrative fewer-than-20-training-actions support flag. That flag is not a sufficiency test. The 64-match historical tournament remains a small, selected training set with sparse goal information.

The model misses off-ball positioning, defenders, pass difficulty, tactical context, much defensive contribution and individual failed-action costs. Carries are provider-derived observed movements, not successful take-ons. Rebounds are not followed after shots. Restarts and entire restart-origin possessions are outside the movement scope. Same-zone moves score zero. Goals and provider non-penalty xG are displayed separately, not added to xT.

Do not use the resulting rank as overall player impact, intrinsic ability, transfer value, future performance or a standalone hiring/recruitment recommendation. Role definitions, playing exposure, opponent mix, team progression and tactical assignments affect comparisons. A public case study should preserve those limitations and source attribution.
