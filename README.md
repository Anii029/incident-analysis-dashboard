# 📊 Incident Analysis Dashboard

An interactive **Incident Management Dashboard** built using **Streamlit** to analyze and visualize IT Service Management (ITSM) data.

---

## 🚀 Live Demo

https://incident-analysis-dashboard-6wfwhkqddtiz5vxdmvdzyr.streamlit.app/

---

## 📌 Project Overview

This project processes raw **incident event log data** and transforms it into a structured dataset to generate meaningful insights.

The dashboard helps in analyzing:

* 📈 Incident trends over time
* ⏱ SLA performance (Met vs Breached)
* 🔥 Priority distribution
* 📂 Top incident categories
* ⏳ Average resolution time
* 📊 Priority vs SLA relationship

---

## 🧠 Key Concepts Used

* Data Cleaning (handling duplicates & hidden missing values like `?`)
* Data Transformation (event logs → structured dataset)
* Feature Engineering (Resolution Time calculation)
* Data Visualization (Matplotlib & Seaborn)
* Interactive Dashboard Development (Streamlit)

---

## 🛠 Tech Stack

* Python 🐍
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## 📂 Dataset

* Source: Kaggle - Incident Event Log Dataset
* Contains multiple lifecycle records per incident

---

## 🔄 Data Processing Steps

1. Removed duplicate records (kept latest state per incident)
2. Replaced hidden missing values (`?`, blanks)
3. Selected relevant columns
4. Converted date columns to datetime format
5. Created **Resolution Time** feature
6. Cleaned categorical fields (Priority, SLA Status)

---

## 📊 Dashboard Features

### 🎛 Filters

* Category filter
* Priority filter

### 📈 Visualizations

* Incident Trend (Line Chart)
* SLA Distribution (Pie Chart)
* Priority Distribution (Bar Chart)
* Category Analysis (Top 10 Categories)
* Priority vs SLA Heatmap

### 📊 Key Metrics

* Total Incidents
* SLA Met %
* Average Resolution Time

---

## 🔍 Key Insights

* A portion of incidents fail to meet SLA targets
* High-priority incidents tend to have higher SLA breach rates
* Certain categories contribute most to incident volume
* Resolution time varies across priority levels

---

## 📸 Screenshots

*<img width="1841" height="869" alt="Screenshot 2026-04-26 151235" src="https://github.com/user-attachments/assets/dff634b4-d23d-4fdf-953d-50e67ad6f0fa" />
<img width="1905" height="1079" alt="Screenshot 2026-04-26 151257" src="https://github.com/user-attachments/assets/a3ff6a06-1081-44f8-b835-ade0cc642252" />
<img width="1876" height="1055" alt="Screenshot 2026-04-26 151311" src="https://github.com/user-attachments/assets/b5b0803c-0e3f-4d93-b39f-382fdbf9b713" />
<img width="1878" height="1022" alt="Screenshot 2026-04-26 151331" src="https://github.com/user-attachments/assets/a2aef4b2-272a-4f46-a5ef-128322ec913e" />
<img width="1908" height="1069" alt="Screenshot 2026-04-26 151215" src="https://github.com/user-attachments/assets/d3532876-bdfb-44b8-86bf-3946abb2d039" />

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run incident_dashboard.py
```

---

## 📦 Requirements

```
streamlit
pandas
matplotlib
seaborn
```

---

## 📌 Future Improvements

* Add date range filter
* Include assignment group analysis
* Track SLA trends over time
* Improve UI styling

---

## 👨‍💻 Author

**Anitha Nallapati**
GitHub: https://github.com/Anii029

---

## ⭐ Acknowledgment

Inspired by real-world **ServiceNow / ITSM analytics use cases**.
