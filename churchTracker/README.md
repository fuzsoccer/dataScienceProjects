# ⛪ Church Attendance & Engagement Analytics

## 🧠 Overview

This project analyzes church attendance and event data to identify trends in participation, engagement, and growth over time.

Using data extracted from church management systems (e.g., Planning Center), the project focuses on transforming raw attendance records into structured insights that support **operational decision-making and community engagement strategies**.

---

## 🎯 Problem Statement

Church organizations often track attendance across multiple services, groups, and events. However:

- Data is fragmented across events and dates  
- Attendance trends are not always obvious  
- Comparing engagement across groups can be difficult  
- Manual reporting is time-consuming  

This project aims to:

- Aggregate attendance data across events and time  
- Identify trends and patterns in participation  
- Provide a data-driven foundation for decision-making  

---

## ⚙️ Methodology

### 1. Data Collection
- Attendance data is retrieved from church management systems (e.g., Planning Center API)  
- Data includes:
  - Event dates  
  - Group/service names  
  - Attendance counts  

---

### 2. Data Processing
- Clean and standardize raw attendance data  
- Remove future or canceled events  
- Ensure consistent time intervals (weekly aggregation)  

---

### 3. Feature Engineering
- Derive metrics such as:
  - Weekly attendance totals  
  - Attendance trends over time  
  - Growth or decline rates  

---

### 4. Exploratory Data Analysis (EDA)
- Analyze attendance trends across time  
- Identify seasonal patterns or anomalies  
- Compare engagement across groups or services  

---

### 5. Visualization
- Time-series plots of attendance over time  
- Trend lines using regression models  
- Weekly attendance breakdowns  

---

## 📊 Example Outputs

- Weekly attendance trend charts  
- Growth/decline analysis over time  
- Comparative attendance across groups  
- Smoothed trend lines for long-term insights  

---

## 🧰 Technical Stack

- **Language:** Python  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Requests (API integration)  

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/fuzsoccer/dataScienceProjects.git
cd dataScienceProjects/churchTracker
