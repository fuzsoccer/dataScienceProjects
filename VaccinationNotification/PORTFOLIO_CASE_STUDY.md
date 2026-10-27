# Do personalized risk messages increase flu vaccination?

## Project overview

A message can increase attention without changing behavior. This project uses deidentified data from an existing randomized field study to examine whether telling patients they are at high risk for influenza and its complications improves recorded vaccination uptake, and whether more elaborate explanations add value.

The Python analysis covers 42,481 patients retained in the study's manuscript analysis population. It combines data auditing, experiment analysis, model replication, and sensitivity checks. This is a secondary analysis of researchers' data, not a trial I designed or conducted.

## Questions

1. Do high-risk messages improve vaccination compared with a basic reminder or no message?
2. Does adding medical-record or algorithm-based explanations improve uptake beyond a high-risk message alone?
3. Does giving three personalized reasons work better than giving one?

## Approach

I separated the archive's manuscript and registry releases, documented the chosen files, and checked treatment labels against the supplied dictionary and analysis code. I verified that identifiers were unique, outcomes were binary, and the analysis population matched the full file's exclusion flags. Missing values in message-specific fields were retained rather than treated as grounds for dropping otherwise valid observations.

The main analysis compares five messaging groups and reports absolute differences in vaccination probability. I reproduced four source linear probability models, added HC1 robust confidence intervals, and independently checked the conventional Python estimates against R. I examined baseline balance, adjusted for risk strata, and checked how conclusions changed under alternative population definitions. Logistic models supplied an additional sensitivity check.

Within the medical-record and algorithm arms, I analyzed the randomized one-versus-three reasons comparison using an interaction model. This distinguishes the effect within each framing from whether the two effects differ.

## Findings

Recorded vaccination ranged from 31.51% in passive control to 34.57% in the high-risk-only arm. The pooled high-risk arms exceeded passive control by **2.57 percentage points** (95% robust interval: **1.42 to 3.71**). That is about 26 more recorded vaccinations per 1,000 analyzed patients, expressed as an absolute difference rather than a relative percentage increase.

Against active control, however, the pooled difference was **1.14 points**, with an interval from **-0.01 to 2.30**. Its advantage over a basic reminder was less certain. The high-risk-only arm had the highest observed rate, but this alone does not establish it as the best message.

Adding reasons did not clearly improve uptake over high-risk messaging alone. Within the two reasons arms, sending three rather than one reason produced an equal-arm average difference of **-0.70 points** (95% interval: **-2.12 to 0.73**). The interaction between framing and reasons count was also uncertain. These data provide no clear evidence of an incremental benefit from additional reasons; they do not prove equivalence.

The main risk-message comparison with passive control remained positive across the populations examined. Baseline differences on the measured characteristics were small, and risk adjustment changed the main estimates very little.

## Interpretation and limitations

The results support further evaluation of targeted high-risk outreach, while leaving its incremental advantage over a standard reminder less certain. The analysis does not establish that more detailed explanations are better. It also does not identify the psychological mechanism behind vaccination decisions.

The main population excludes some enrolled patients, and exclusion rates differed between reasons-count assignments. Shared addresses create potential dependence or spillovers, but household identifiers are unavailable. Recorded outcomes may not capture every vaccination. Outreach-channel and SMS-timing comparisons should not be interpreted as randomized experiments.

This portfolio work was developed after inspecting the data. Its Holm adjustments are additional conservative analyses, and correction is performed within stated comparison families rather than globally across every result. The non-preregistered 29-day endpoint and sensitivity checks are supporting analyses, not independent evidence. Conclusions concern the studied patient population and messaging context.

## Reproducible deliverables

- Three Python analysis scripts, pinned dependencies, and a self-contained notebook with saved code, tables, and charts.
- Data dictionaries, file hashes, exclusion audits, baseline balance tables, and model outputs.
- Vaccination-rate and reasons-effect charts with confidence intervals.
- Independent R validation scripts and saved reference results.

The project demonstrates how to move from a downloaded research archive to an auditable multi-arm experiment analysis while keeping observed differences, statistical uncertainty, and causal limitations distinct.

## Attribution and status

Original study and data: Gail M. Rosenbaum and colleagues; study NCT05009251. The manuscript release and source code were supplied in `mqbux-osfstorage-archive.zip`. This case study summarizes the reproduced models; it is not a full replication of every published result. Source reconciliation is documented in reports/source_reconciliation.md. The main numerical results agree, with stated sign/estimand and manuscript-text discrepancies. Complete verbatim messages were not retrievable; no full wording is claimed as verified. The publication package excludes patient-level data and third-party documents and provides source acquisition instructions instead.
