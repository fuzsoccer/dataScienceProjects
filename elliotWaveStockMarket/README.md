# 📈 Elliott Wave Detection & Time-Series Signal Extraction

## 🧠 Overview

This project implements a signal-processing pipeline to identify and approximate **Elliott Wave structures** in financial time series data.

Elliott Wave Theory suggests that financial markets move in recurring patterns driven by investor psychology, typically consisting of **5 impulse waves followed by 3 corrective waves**.  [oai_citation:0‡Angel One](https://www.angelone.in/knowledge-center/share-market/elliott-wave-theory?utm_source=chatgpt.com)  

This project translates that qualitative theory into a **quantitative, algorithmic framework** using peak detection, feature engineering, and rule-based filtering.

The goal is to transform noisy price data into structured signals that can support **analysis, visualization, and future predictive modeling**.

---

## 🎯 Problem Statement

Financial time series data is:

- Noisy and non-linear  
- Difficult to segment into meaningful structures  
- Challenging to interpret consistently using manual techniques  

Traditional Elliott Wave analysis is:

- Subjective and analyst-dependent  
- Not scalable  
- Difficult to validate  

This project aims to:

- Detect turning points in price data algorithmically  
- Enforce structural constraints based on wave theory  
- Create a reproducible framework for wave identification  

---

## ⚙️ Methodology

### 1. Data Collection
- Historical stock price data retrieved using `yfinance`  
- Monthly aggregation used to reduce noise and highlight long-term trends  

---

### 2. Signal Processing

- Local maxima (peaks) and minima (troughs) detected using:
  - `scipy.signal.find_peaks`  
- Dynamic prominence threshold based on price volatility  
- Ensures detection adapts across different stocks and price scales  

---

### 3. Structural Filtering

- Peaks and troughs are merged and sorted chronologically  
- A custom algorithm enforces **alternating directionality**:
  - peak → trough → peak  

This aligns with Elliott Wave structure, where markets alternate between upward and downward movement driven by sentiment cycles.  [oai_citation:1‡Industri UMA](https://industri.uma.ac.id/2023/02/15/introduction-to-elliott-wave-theory/?utm_source=chatgpt.com)  

---

### 4. Wave Approximation

- Up to 9 turning points are selected  
- Labeled as:
  - Impulse waves: `0–5`  
  - Corrective waves: `A–C`  

This reflects the standard **5–3 wave cycle** used in Elliott Wave Theory  

---

### 5. Trend Detection

- Simple trend classification:
  - Uptrend or downtrend based on price movement  
- Provides context for interpreting wave structure  

---

### 6. Visualization

- Time series plotted with:
  - Annotated wave labels  
  - Highlighted turning points  
- Enables visual validation of detected structures  

---

## 📊 Insights & Findings

- Peak and trough detection identifies major turning points in long-term price series, enabling segmentation of market cycles  
- Detected wave structures exhibit alternating patterns consistent with expected market behavior (uptrend vs corrective phases)  
- Monthly aggregation reduces short-term noise, allowing clearer identification of structural trends  
- Limiting wave points to key turning points simplifies complex time series into interpretable segments  
- The approach demonstrates how noisy financial data can be transformed into structured signals using rule-based methods

---

## 🤖 Model Output / Decision Framework

- Detected wave structures are used to classify the current market phase:
  - Impulse phase (trend continuation)  
  - Corrective phase (potential reversal)  

- The most recent wave point is used as a signal for potential trend direction:
  - Upward movement → bullish signal  
  - Downward movement → bearish signal  

### Decision Use Case

- Identify potential entry/exit points based on wave phase  
- Generate rule-based signals for trend continuation or reversal  
- Serve as feature input for predictive financial models  

---

## 💡 Implications & Applications

- Provides a systematic approach to identifying market cycles without manual labeling  
- Enables development of rule-based trading signals based on detected wave structures  
- Supports feature engineering for machine learning models (e.g., trend phase, wave length, reversal points)  
- Demonstrates how signal processing techniques can be applied to financial time series data

---

## 📊 Example Outputs & Visualizations

- Monthly stock price time series with detected peaks and troughs  
- Annotated Elliott Wave approximation with labeled wave points (0–5, A–C)  
- Visualization of turning points representing major market movements  
- Simplified structural representation of price trends derived from noisy data

---

## 🧰 Technical Stack

- **Language:** Python  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - SciPy (`find_peaks`)  
  - Matplotlib  
  - yfinance  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects/elliotWaveStockMarket
