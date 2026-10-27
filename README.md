# 📊 Data Science Projects

A collection of applied data science projects focused on **time-series analysis, statistical modeling, causal inference, predictive machine learning, and visualization using real-world data**.

This repository showcases practical implementations of data science techniques using Python, with an emphasis on transforming noisy datasets into structured, actionable insights.

---

## 🧠 Overview

This repository serves as a portfolio of hands-on data science work, demonstrating:

- Time-series analysis and segmentation  
- Signal processing techniques applied to financial data  
- Statistical modeling and feature engineering  
- Randomized experiments and A/B testing  
- Predictive machine learning and model evaluation  
- Visualization for insight generation  
- End-to-end analytical workflows  

Projects are developed in a notebook-first format to support iterative exploration, validation, and refinement.

---

## ⚙️ Technical Stack

- **Languages:** Python  
- **Libraries:** Pandas, NumPy, SciPy, Matplotlib, Scikit-learn, Statsmodels
- **Data Sources:** APIs (e.g., yfinance), structured datasets  
- **Tools:** Jupyter Notebook, Tableau

---

## 📈 Featured Projects

### Elliott Wave Approximation via Signal Processing

This project implements an algorithmic approach to approximate **Elliott Wave structures** in financial time series data.

#### Key Components:

- **Data Ingestion**
  - Historical stock price data retrieved using `yfinance`
  - Monthly aggregation to reduce noise  

- **Signal Processing**
  - Peak and trough detection using `scipy.signal.find_peaks`
  - Dynamic prominence thresholds based on volatility  

- **Structural Filtering**
  - Enforces alternating peak/trough sequence  
  - Filters noise to identify meaningful turning points  

- **Wave Labeling**
  - Identifies up to 9 wave points (0–5 impulse, A–C correction)  
  - Labels structural segments of the time series  

- **Visualization**
  - Annotated plots of price series with detected wave structure  

#### Key Focus:

- Time-series segmentation  
- Feature extraction from noisy financial data  
- Rule-based modeling and pattern detection

### Oregon Medicaid Lottery and Emergency Department Use

This project examines whether selection in Oregon’s Medicaid lottery changed the probability of an emergency department visit.

Using public-use data from the Oregon Health Insurance Experiment, the analysis distinguishes the effect of being offered the opportunity to apply for Medicaid from the effect of obtaining insurance.

#### Key Components:

- **Data Preparation**
  - Linked lottery assignment, household information, and emergency department records
  - Validated the analysis sample and key variables

- **Statistical Analysis**
  - Estimated the intention-to-treat effect of lottery selection
  - Accounted for household size and baseline emergency department use
  - Used household-clustered standard errors and sensitivity analysis

- **Visualization**
  - Created Python figures and an interactive Tableau dashboard
  - Compared descriptive group differences with adjusted estimates

#### Main Finding:

Lottery selection increased the estimated probability of any recorded emergency department visit by **1.72 percentage points** (95% confidence interval: **0.56–2.88 percentage points**) in the study sample.

#### Key Focus:

- Randomized experiments and causal inference
- Regression adjustment and statistical uncertainty
- Clear communication of findings and limitations

[Explore the project](./OregonMedicaidED/)

### Hospital Readmission Prediction

This project predicts **recorded inpatient readmission in less than 30 days** among encounters involving patients with diabetes who are discharged home, using historical UCI hospital data.

#### Key Components:

- **Data Preparation**
  - Defined a home-discharge cohort and reviewed missing values
  - Kept each patient's encounters within one training, validation, or test group

- **Predictive Modeling**
  - Compared a constant-risk baseline, logistic regression, and a random forest
  - Fitted preprocessing on training data only
  - Retained logistic regression because the forest's validation improvement fell below the predefined practical requirement

- **Evaluation and Visualization**
  - Assessed ranking, probability calibration, and performance at an illustrative 20% review capacity
  - Estimated uncertainty using a patient-level bootstrap
  - Created Python figures and a Tableau companion dashboard using aggregate results

#### Main Finding:

On **14,653 reserved test encounters**, logistic regression achieved a **ROC AUC of 0.657**. Reviewing the highest-scoring **20%** flagged **38.9% of recorded readmissions**, with **18.9% precision**. These findings describe historical prediction performance; they do not establish that follow-up would prevent readmissions.

#### Key Focus:

- Classification and interpretable predictive modeling
- Patient-aware validation and data leakage prevention
- Model comparison, uncertainty, and operational trade-offs

[Explore the project](./HospitalReadmissions/)

### Vaccination Messaging: Multi-Arm A/B Testing

This project analyzes an existing **five-arm randomized vaccination messaging study**, using **42,481 patients** retained in the manuscript analysis population.

It examines whether personalized high-risk messages improve recorded influenza vaccination compared with a basic reminder or no outreach, and whether medical-record explanations, algorithm framing, or additional personalized reasons add value.

#### Key Components:

- Data integrity, missingness, exclusion, and baseline balance checks
- Source-aligned regression models with robust confidence intervals and multiple-comparison adjustments
- Risk-stratum adjustment, alternative analysis populations, and logistic sensitivity checks
- A randomized one-versus-three reasons interaction analysis
- A self-contained notebook with inline code, saved tables, and charts; conventional estimates independently validated against R

#### Main Finding:

Pooled high-risk messages exceeded no outreach by **2.57 percentage points** (95% robust confidence interval: **1.42–3.71 percentage points**). Their **1.14-point** advantage over a basic reminder remained uncertain, and sending three reasons rather than one showed no clear benefit. Conclusions account for analysis exclusions and possible household effects; non-significant results do not establish equivalence.

#### Key Focus:

- Multi-arm A/B testing and randomized experiment analysis
- Treatment interactions, effect sizes, and statistical uncertainty
- Reproducible analysis and transparent source attribution

[Explore the project](./VaccinationNotification/) · [View the notebook](./VaccinationNotification/notebooks/01_study2_eda.ipynb)

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects
```

Follow each project's README for its data requirements, dependencies, and instructions.
