# Methodology and research limits

## Scope and provenance

Two independent branches support the portfolio. StatsBomb supplies named-player events for a later recruitment analysis. Metrica supplies anonymized tracking for engineering and spatial methodology. Do not join anonymous shirt IDs to named players, or treat StatsBomb event coordinates/360 snapshots as continuous tracking. The small Metrica sample cannot support generalizable player valuation.

The first fetch resolves each upstream master branch to a commit and records file hashes. Subsequent fetches use those commits; they do not silently update data. To update deliberately, create a new data root and retain the old lock. Exact dependency-free analysis is repeatable with a recorded Python version; outputs may differ in insignificant float formatting across versions. Tracking is streamed. Calculations and summaries use all frames; the default export retains every 25th frame for storage. This is subsampling of the output, not of velocity estimation. Exported step distances cannot be summed to reconstruct full distance. Use the summary or export stride 1.

## Tracking definitions

Coordinate origin remains the provider's top-left with y increasing downward. Field size 105 by 68 meters follows Metrica's README. No attacking-direction inference is made. Out-of-pitch positions are flagged, not clipped: players and ball can legitimately leave the pitch.

For a player at time t:

- Position: `(105*x, 68*y)` in meters.
- Step distance: Euclidean displacement from the immediately preceding frame, only within the same period, with complete finite coordinates at both ends, frame increment 1, and `0 < dt <= 0.2` seconds.
- Speed: step distance divided by dt. Intervals above 12 m/s are rejected and counted; this is a configurable-in-code heuristic, not a provider accuracy guarantee. The next valid step starts at the current observed position, so a spike can invalidate two intervals.
- Ball distance: instantaneous Euclidean distance to a finite observed ball position. This does not establish possession, pressure, or an off-ball run.
- Distance and valid seconds: sums over accepted intervals only. Mean speed is total accepted distance divided by accepted time. Maximum speed is a noise-sensitive diagnostic.
- High-speed seconds: accepted dt where speed is at least 7 m/s, an illustrative threshold. This is time above threshold, not sprint count or calibrated physical workload.
- Position coverage: complete observed player frames divided by all team frames in the file. It is not percentage of playing minutes tracked. Players substituted in/out naturally have lower values.

Missing coordinates are never interpolated. Halftime never contributes a movement interval. Backward differences only use information available at time t. No centered smoothing is used; raw frame differencing amplifies location noise. Validate causal smoothing and threshold sensitivity before physical-performance claims. Speed rejection also removes distance and duration, which can bias summaries downward. Always show rejected counts and observed duration.

Quality gates reject duplicate/unordered frames, invalid within-period time steps/frame gaps, half-missing player coordinate pairs, duplicate event IDs, invalid StatsBomb locations and empty inputs. Full missing player positions, missing ball coordinates, off-pitch positions and rejected speeds remain review flags. Structural success does not certify data suitability. Review missingness by player, period and phase before modeling.

## Event branch

The first player-match table is an inspection baseline. Pass completion follows absence of `pass.outcome`; shots and pressures use event types; xG is the provider's supplied estimate, not a model trained here. No playing-time normalization or possession adjustment is performed. Event counts and provider xG should not be mistaken for intrinsic player quality. Confirm competition, gender, season, coverage and selection mechanism before comparisons.

## Leakage-aware validation design

Define the decision timestamp, role, eligible cohort, target horizon and outcome first. A later model could predict next-season role-adjusted contribution from only prior-season observations. Target and feature windows must not overlap. Exclude later transfers, future minutes, end-of-season aggregates and retrospectively available financial data from earlier scouting decisions.

Use chronological train/validation/test seasons and hold out the latest eligible period once. Fit imputers, scalers, feature selection and hyperparameters on training folds only. Account for overlapping rolling windows: purge overlapping target periods and apply an appropriate gap. Keep all events/frames of a match or possession together. Random frame splits leak nearly identical observations; a random row split is inappropriate.

Evaluate two distinct questions: temporal generalization to future performances of known players, and generalization to unseen players using player-group holdouts. Disjoint-player splits answer a different question from real repeat scouting; report both where feasible. Cluster uncertainty by player and match rather than pretending individual frames are independent. Compare a simple historical-performance baseline, report calibration/error by role and minutes, and check cohort/league shifts. Estimate uncertainty with enough independent units; do not bootstrap adjacent frames as independent matches.

For Metrica, one or two matches are demonstrations only. Even a held-out half or second sample match does not establish robust generalization. A synchronized event/tracking outcome experiment would require auditing frame alignment and a decision-time cutoff; this starter downloads Metrica events for inspection but does not claim alignment or possession labeling.

## Honest portfolio claim

"Built a reproducible football analytics pipeline with pinned public data, automated quality checks and causal movement features; designed a leakage-aware recruitment validation protocol."

Avoid claiming discovered undervalued professionals, validated recruitment ROI, measured pressure quality, or trained a reliable tracking model. Establish those results only with suitable data and evaluation.
