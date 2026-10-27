# Study 2: initial data audit and EDA

This document preserves the initial EDA. Later design verification and model extensions are in `design_and_robustness.md`; those updates supersede the initial statements that reasons randomization and protocol details were unverified.

## Population and treatment groups

The source R script reports 45,164 randomized patients, of whom 103 died before the first message and were not considered enrolled. The full CSV contains 45,061 enrolled patients. The analysis CSV contains 42,481 patients and 16 columns. IDs are unique within each file and the analysis IDs exactly match full-file records without an exclusion reason. Treatment, risk classification, and primary outcomes agree across those matched records.

| Stored treatment | Dictionary meaning | Analyzed N | Vaccinated | Rate |
|---|---|---:|---:|---:|
| nocontact | Passive control | 8,466 | 2,668 | 31.51% |
| control | Active control | 8,522 | 2,807 | 32.94% |
| unspecified | High risk only | 8,498 | 2,938 | 34.57% |
| medrec | High risk medical records + reasons | 8,470 | 2,887 | 34.09% |
| algorithm | High risk algorithm + reasons | 8,525 | 2,863 | 33.58% |

Enrolled arm sizes range from 9,003 to 9,017. This is descriptively close to equal allocation. The generated equal-allocation diagnostic is provisional because allocation probabilities and the full randomized population have not been verified. Similar sizes alone do not verify randomization.

## Variables and interpretation

| Role | Variables | Notes |
|---|---|---|
| Identifier | s_ID | Randomly generated; its prefix is not a study indicator |
| Messaging assignment | algo_condition | Five arms above |
| Underlying risk | risk_condition | top3: top 3%; top10: top 4–10% in manuscript dictionary; not a randomized exposure |
| Message content | num_reasons | 1reason or 3reasons, present only in medrec/algorithm; randomization of count not verified |
| Demographics | sex, race, ethnicity, age65plus, age_bin | EHR categories; age is grouped |
| Outreach | modalities, sms_date_bin | Letter/portal/SMS combinations; early/late SMS where applicable |
| Other descriptors | dup_address, geis_pcp | Shared-address indicator and Geisinger primary-care indicator |
| Primary endpoint | vaccinated | Binary recorded vaccination in the primary window |
| Additional robustness endpoint | vaccinated_4weeks | Enrollment day plus next 4 weeks (29 days) |
| Outcome provenance | vax_source | EHR_data or Non_EHR_data for vaccinated patients |

The full file additionally contains `modalities_orig`, `letter_sent`, `portal_sent`, `sms_sent`, and `exclude_reason`. In passive control, outreach flags describe eligibility, not actual contact. The aggregate time file is daily counts, not an additional patient-level sample.

## Quality, missingness, and exclusions

There are 2,580 enrolled exclusions (5.73%): early vaccination 1,096; protective risk reasons 816; contraindication 563; death during study 105. Arm exclusion rates range from 5.45% to 6.11%. The R script's 103 pre-enrollment deaths are separate from these 105 deaths during study. Exclusions after randomization limit a simple intention-to-treat interpretation.

Primary and four-week outcomes contain only 0/1 and have no missing values in the supplied analysis file. This does not establish perfect capture of vaccinations outside the available records. Four-week positives are a subset of primary-window positives.

Missing values are concentrated in three fields: num_reasons 25,486; sms_date_bin 21,163; vax_source 28,318. Reasons count is absent outside the two reasons arms. SMS timing is absent for passive control and other records without an applicable timing value; do not impute a timing group. Vaccine-source missingness exactly corresponds to vaccinated=0. Do not drop rows globally because these fields are blank.

The cohort includes 28,699 patients under 65 and 13,782 aged 65+, 28,766 recorded female and 13,715 recorded male, and 12,813 in the top3 risk group versus 29,668 in top10. About 17.61% share an address with another study patient. Categorical distributions by arm are exported for further balance assessment; a full balance analysis is not yet complete.

## Exploratory comparisons

Against passive control, observed absolute differences are +1.42 percentage points for active control, +3.06 for high risk only, +2.57 for medical records + reasons, and +2.07 for algorithm + reasons. With Holm adjustment across the seven exported comparisons, the three high-risk arm comparisons against passive control have p<0.05; active control does not.

Pooling the three high-risk arms versus active control yields +1.14 percentage points (individual 95% CI −0.01 to +2.30; unadjusted p=0.0537; Holm p=0.1883). Algorithm versus medical-record wording yields −0.50 points (95% CI −1.92 to +0.92). There is no clear evidence of algorithm wording superiority in this initial comparison. High risk only has the highest observed rate, but these results do not establish it as superior to the other high-risk messages.

These are unadjusted analysis-population estimates under a patient-independence assumption, not final causal conclusions or clinical recommendations. The five-arm design is a multi-arm experiment rather than a simple two-group A/B test. See the README for protocol checks and planned extensions.

Final review: the 29-day outcome is a non-preregistered robustness check, distinct from the registered later vaccination endpoint. Source-message and published-number reconciliation is in `source_reconciliation.md`. Raw source files and PDFs are retained only in the complete working package; obtain them upstream when using the publication package.
