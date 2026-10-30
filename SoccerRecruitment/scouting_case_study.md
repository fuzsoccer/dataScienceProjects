# Role-based scouting review: 2022 World Cup

<img src="assets/statsbomb-logo.png" alt="StatsBomb — event data source" width="240">

## Decision and scope

Identify players meriting further review for a specified contribution style. This is a retrospective tournament case study, not a current transfer shortlist, causal impact assessment or financial undervaluation claim. StatsBomb Open Data provides the event evidence; movement xT uses a model fitted on 2018 and applied to 2022.

Eligibility requires at least 300 elapsed minutes and 50% positioned-event share in the role, complete eligible-movement xT coverage and a scored movement. Role assignments are event-based; metrics cover all roles played. Up to three distinct players are selected sequentially per role, using separate lenses rather than an overall score. Striker shot quality additionally requires 5 non-penalty shots. Later lenses select the best remaining player; selection order therefore affects the result.

## Role definitions

- Striker: Center Forward, Left Center Forward, Right Center Forward, Secondary Striker.
- CM: Center Midfield, Left Center Midfield, Right Center Midfield.
- Winger: Left Wing, Right Wing.

## Striker review candidates

Eligible reference pool: 14 player-team profiles.

| Player | Team | Review lens | Primary measure | Minutes |
|---|---|---|---|---:|
| Breel-Donald Embolo | Switzerland | Chance generation | npxG/90: 0.631 | 341.1 |
| Olivier Giroud | France | Shot volume | NP shots/90: 3.383 | 452.2 |
| Richarlison de Andrade | Brazil | Shot quality | npxG/shot: 0.202 | 336.5 |

### Breel-Donald Embolo: Chance generation

**Evidence:** Highest npxG/90 among remaining eligible Striker profiles. Recorded 0.631 for the primary measure across 4 appearances; role-event share 100.0%.

**Review flags:** Fewer than 450 elapsed minutes; Fewer than five appearances.

**Next scouting check:** Review shot locations, supply and club-season non-penalty xG; separate open-play and set-piece chances.

### Olivier Giroud: Shot volume

**Evidence:** Highest NP shots/90 among remaining eligible Striker profiles. Recorded 3.383 for the primary measure across 6 appearances; role-event share 100.0%.

**Review flags:** No heuristic flags triggered; sample/model limitations remain.

**Next scouting check:** Review shot quality, blocked/long-range attempts, team possession and repeatability across a club season.

### Richarlison de Andrade: Shot quality

**Evidence:** Highest npxG/shot among remaining eligible Striker profiles; at least 5 NP shots required. Recorded 0.202 for the primary measure across 4 appearances; role-event share 100.0%.

**Review flags:** Fewer than 450 elapsed minutes; Fewer than five appearances; One match contributes over half of positive movement xT.

**Next scouting check:** Review the individual shots and service patterns; a minimum of five shots remains a very small finishing sample.

## CM review candidates

Eligible reference pool: 12 player-team profiles.

| Player | Team | Review lens | Primary measure | Minutes |
|---|---|---|---|---:|
| Pedro González López | Spain | Forward progression | Forward passes (10 units)/90: 22.903 | 389.0 |
| Mateo Kovačić | Croatia | Chance creation | NP xG assisted/90: 0.168 | 682.2 |
| Yunus Dimoara Musah | United States | Carrying value | Carry xT/90: 0.033 | 379.0 |

### Pedro González López: Forward progression

**Evidence:** Highest Forward passes (10 units)/90 among remaining eligible CM profiles. Recorded 22.903 for the primary measure across 4 appearances; role-event share 100.0%.

**Review flags:** Fewer than 450 elapsed minutes; Fewer than five appearances; One match contributes over half of positive movement xT.

**Next scouting check:** Review under-pressure passes, receiver advantage, opponent block and possession-adjusted progression.

### Mateo Kovačić: Chance creation

**Evidence:** Highest NP xG assisted/90 among remaining eligible CM profiles. Recorded 0.168 for the primary measure across 7 appearances; role-event share 76.0%.

**Review flags:** One match contributes over half of positive movement xT.

**Next scouting check:** Inspect linked shots and dead-ball share; test whether creation persists across teammates, opponents and a longer sample.

### Yunus Dimoara Musah: Carrying value

**Evidence:** Highest Carry xT/90 among remaining eligible CM profiles. Recorded 0.033 for the primary measure across 4 appearances; role-event share 72.6%.

**Review flags:** Fewer than 450 elapsed minutes; Fewer than five appearances.

**Next scouting check:** Review positive and negative movements, failed take-ons and possession losses with video; event xT misses defenders and off-ball context.

## Winger review candidates

Eligible reference pool: 20 player-team profiles.

| Player | Team | Review lens | Primary measure | Minutes |
|---|---|---|---|---:|
| Salem Mohammed Al Dawsari | Saudi Arabia | Carrying value | Carry xT/90: 0.093 | 321.2 |
| Raphael Dias Belloli | Brazil | Chance creation | NP xG assisted/90: 0.372 | 338.7 |
| Kylian Mbappé Lottin | France | Shooting threat | npxG/90: 0.347 | 691.2 |

### Salem Mohammed Al Dawsari: Carrying value

**Evidence:** Highest Carry xT/90 among remaining eligible Winger profiles. Recorded 0.093 for the primary measure across 3 appearances; role-event share 63.4%.

**Review flags:** Fewer than 450 elapsed minutes; Fewer than five appearances; One match contributes over half of positive movement xT; Within-role movement rank changes by at least five places across grids.

**Next scouting check:** Review positive and negative movements, failed take-ons and possession losses with video; event xT misses defenders and off-ball context.

### Raphael Dias Belloli: Chance creation

**Evidence:** Highest NP xG assisted/90 among remaining eligible Winger profiles. Recorded 0.372 for the primary measure across 5 appearances; role-event share 66.0%.

**Review flags:** Fewer than 450 elapsed minutes.

**Next scouting check:** Inspect linked shots and dead-ball share; test whether creation persists across teammates, opponents and a longer sample.

### Kylian Mbappé Lottin: Shooting threat

**Evidence:** Highest npxG/90 among remaining eligible Winger profiles. Recorded 0.347 for the primary measure across 7 appearances; role-event share 85.3%.

**Review flags:** No heuristic flags triggered; sample/model limitations remain.

**Next scouting check:** Review chance quality and team usage, plus a longer club sample and video of off-ball movement.

## Interpretation and limits

Role-pool percentiles describe the observed eligible cohort, not player ability. Grid sensitivity applies to movement xT only. Goal/shot and event-count metrics are not validated by that analysis. Temporary injury absences and stoppage time follow the documented elapsed-participation convention. Team possession, tactics, opponents, game state, pass difficulty and off-ball influence remain unadjusted. These filters and heuristic flags do not establish reliability, even when none trigger.

World Cup participation and progression select players and exposure; the cohort cannot represent the full recruitment market. Transfer feasibility needs a real club brief, longer club data, video, age, injuries, fees/wages, contracts and availability. Future predictive claims require a separately specified target and untouched temporal evaluation. Do not tune on the 2022 findings and continue calling that cohort untouched.

Data source: StatsBomb Open Data. Follow the provider README/license and required acknowledgement/logo guidance before publication. Model inspiration and explicit variant assumptions are documented in notebook 06.
