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

## 📊 Insights & Findings

- Weekly attendance trends can be clearly identified after aggregating event-level data into consistent weekly intervals  
- Attendance varies across groups, with some groups showing stable participation while others exhibit higher variability  
- Linear trend modeling reveals whether individual groups are growing or declining over time  
- Removing canceled and future events ensures more accurate representation of historical attendance patterns  
- Standardizing time intervals (weekly aggregation) enables consistent comparison across groups and time periods

---

## 💡 Implications & Applications

- Enables leadership to monitor attendance trends and identify growth or decline across groups  
- Supports data-driven decisions for staffing, scheduling, and resource allocation  
- Identifies groups with inconsistent engagement for targeted outreach and improvement  
- Provides a foundation for forecasting future attendance and planning capacity needs

---

## 🤖 Model Output / Decision Framework

- A linear trend model is applied to weekly attendance to estimate growth or decline over time  
- The slope of the regression line represents weekly change in attendance (e.g., +2 attendees per week)  
- Groups can be classified as:
  - Growing (positive slope)  
  - Stable (near-zero slope)  
  - Declining (negative slope)  

### Decision Use Case

- Identify groups that require intervention (declining attendance)  
- Allocate resources to high-growth groups  
- Forecast future attendance for planning and capacity management  

---

## 📊 Example Outputs

- Event-level attendance dataset aggregated from Planning Center API  
- Weekly attendance summaries by group, enabling time-series analysis  
- CSV outputs:
  - `group_event_attendance_raw.csv` (event-level data)  
  - `group_weekly_attendance.csv` (aggregated weekly data)  
- Time-series plots of weekly attendance per group  
- Regression trend lines showing growth or decline in attendance over time  

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
