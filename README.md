# 📊 Data Science Projects

A collection of applied data science projects focused on **time series analysis, statistical modeling, and signal extraction from real-world data**.

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

## 📈 Featured Project

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

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects
