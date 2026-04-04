# ⚾ Fantasy Baseball Analytics & Player Performance Modeling

## 🧠 Overview

This project analyzes fantasy baseball data to evaluate player performance, identify trends, and support decision-making for roster construction and player selection.

The workflow focuses on transforming raw baseball statistics into meaningful insights through **data aggregation, feature engineering, and exploratory analysis**.

---

## 🎯 Problem Statement

Fantasy baseball decision-making is often driven by:

- Raw box score statistics  
- Short-term performance trends  
- Subjective judgment  

However:

- Player performance is highly variable  
- Small sample sizes can be misleading  
- It is difficult to compare players across multiple statistical dimensions  

This project aims to:

- Aggregate and structure player performance data  
- Analyze trends over time  
- Provide a data-driven foundation for evaluating fantasy baseball players  

---

## ⚙️ Methodology

### 1. Data Collection
- Player and game-level data is collected from fantasy baseball sources and APIs  
- Data includes key statistics such as batting averages, counting stats, and performance metrics  

---

### 2. Data Processing
- Clean and standardize raw datasets  
- Handle missing values and inconsistencies  
- Aggregate data at the player level  

---

### 3. Feature Engineering
- Compute derived metrics such as:
  - Batting averages  
  - Rolling performance trends  
  - Comparative statistics across players  

---

### 4. Exploratory Data Analysis (EDA)
- Analyze player performance distributions  
- Identify trends and outliers  
- Compare consistency vs volatility across players  

---

### 5. Visualization
- Generate plots to visualize:
  - Player performance over time  
  - Distribution of key metrics  
  - Comparative player analysis  

---

## 📊 Insights & Findings

- Team performance evolves over the season, with cumulative win percentage providing a more stable indicator of team strength than weekly results  
- Teams with higher cumulative home runs and strikeouts tend to correlate with stronger overall standings, highlighting the importance of power and pitching categories  
- Ranking volatility decreases over time, indicating early-season performance is less predictive than long-term trends  
- Player-level analysis shows significant variability in daily batting averages, reinforcing that short-term performance can be misleading  
- Cumulative batting average stabilizes over time, making it a more reliable performance indicator  
- Differences between current and career averages highlight potential overperformance or regression candidates  

---

## 💡 Implications & Applications

- Enables data-driven roster decisions by focusing on long-term performance rather than short-term fluctuations  
- Helps identify consistent players versus high-variance performers for lineup optimization  
- Supports trade and waiver decisions by identifying regression or breakout candidates  
- Provides a framework for evaluating team strength and competitive positioning over time  

---

## 📊 Example Outputs

- Weekly team rankings based on cumulative win percentage  
- Visualization of team performance trends over time (Wins, Losses, Ties)  
- Cumulative statistics tracking (e.g., Home Runs, Strikeouts) by team  
- Player-level batting performance charts showing daily and cumulative averages  
- Comparison of current player performance vs career batting averages  
- Time-series plots highlighting performance trends and variability across players

---

## 🧰 Technical Stack

- **Language:** Python  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - Matplotlib  
  - (Optional) SciPy / Scikit-learn  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects/FantasyBaseball
