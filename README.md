# 📊 Data Science Projects

A collection of applied data science projects focused on **time-series analysis, statistical modeling, causal inference, and visualization using real-world data**..

This repository showcases practical implementations of data science techniques using Python, with an emphasis on transforming noisy datasets into structured, actionable insights.

---

## 🧠 Overview

This repository serves as a portfolio of hands-on data science work, demonstrating:

- Time-series analysis and segmentation  
- Signal processing techniques applied to financial data  
- Statistical modeling and feature engineering  
- Visualization for insight generation  
- End-to-end analytical workflows  

Projects are developed in a notebook-first format to support iterative exploration, validation, and refinement.

---

## ⚙️ Technical Stack

- **Languages:** Python  
- **Libraries:** Pandas, NumPy, SciPy, Matplotlib, Scikit-learn  
- **Data Sources:** APIs (e.g., yfinance), structured datasets  
- **Tools:** Jupyter Notebook  

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

[Explore the project](./Oregon%20Medicaid%20ED/)

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects
