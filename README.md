# 🏅 Olympic Data Engineering & Analytics Project

A complete data engineering pipeline and dashboarding project using **Azure**, **Databricks**, and **Power BI**. This project processes historical Olympic data using a Bronze-Silver-Gold architecture and presents insights with interactive dashboards.

---

## 🚀 Project Overview

This project was completed as part of a data engineering internship and demonstrates how to:
- Ingest and store data using **Azure Blob Storage**
- Process large volumes of structured data using **Databricks** with PySpark
- Build a multi-layered architecture (Bronze → Silver → Gold)
- Create and share **interactive dashboards** with **Power BI**

---

## 📁 Folder Structure

Olympic-DataEngineering-Project/
├── datasets/ # Raw .csv files (optional or sample data)
├── images/ # Dashboard screenshots
│ ├── Olympic dashboard page1.png
│ └── Olympic Dashboard Page 2.png
├── O_Bronze.py # Bronze Layer script
├── O_Silver.py # Silver Layer script
├── O_Gold.py # Gold Layer script
├── olympicpbi.pdf # Power BI Dashboard export (PDF)
├── olympicp dashboard.pbix # Power BI file
├── LICENSE
└── README.md


---

## ⚙️ Tools & Technologies

| Tool/Service       | Purpose                                 |
|--------------------|------------------------------------------|
| Azure Blob Storage | Hosting and storing raw Olympic CSVs     |
| Azure Databricks   | Processing data using PySpark Notebooks  |
| Python & SQL       | Data transformation & querying           |
| Power BI           | Dashboard creation and data visualization |

---

## 🧱 Architecture: Bronze – Silver – Gold

Azure Blob Storage (.csv)
↓
Bronze Layer (Raw Mount)
↓
Silver Layer (Cleaned/Transformed)
↓
Gold Layer (Aggregated Tables)
↓
Power BI Dashboard


---

## 📜 Description of Processing Layers

### 🔸 Bronze Layer
- Mounts raw Olympic `.csv` data from Azure Blob Storage to Databricks.
- Minimal processing; serves as the raw data zone.

### 🔸 Silver Layer
- Cleans and transforms raw data:
  - Handles nulls
  - Joins tables (athlete, sport, event, medal)
  - Formats columns

### 🔸 Gold Layer
- Generates aggregated insights and analysis-ready tables:
  - Medal counts by athlete, gender, year, and country
  - Total athletes by sport and season
  - Demographic metrics like GDP, population

---

## 📊 Power BI Dashboards

### 🔵 **Page 1 – Summary Overview**

![Dashboard Page 1](images/Olympic%20dashboard%20page1.png)

- 🥇 **Total Medals**: 27,497
- 👥 **Total Athletes**: 19,702
- 📊 Top Sports by Athlete Count
- 🌍 Medals by Country (Treemap)
- 🗺️ GDP by Country (Map)
- 🏅 Medal Counts by Athlete

---

### 🟢 **Page 2 – Gender & Demographics**

![Dashboard Page 2](images/Olympic%20Dashboard%20Page%202.png)

- 👩‍🦱 Gender Distribution of Medals
- 📈 Population by Country
- 📍 Olympic Host Cities (Map)
- 🔎 Filters by Year, Gender, Country, Season

---

## 🧠 Key Learnings

- Real-world **Lakehouse architecture** for data warehousing
- Data ingestion and transformation using **Databricks + PySpark**
- Seamless integration of **Azure data services** with Power BI
- Effective **data storytelling** through dashboards

---

## 📎 Files You Can Explore

| File/Folder            | Purpose |
|------------------------|---------|
| `O_Bronze.py`          | Bronze Layer logic (mount raw data) |
| `O_Silver.py`          | Cleaned and transformed dataset logic |
| `O_Gold.py`            | Aggregated Gold Layer metrics |
| `olympicpbi.pdf`       | View dashboard if you don’t have Power BI |
| `olympicp dashboard.pbix` | Open and interact with the dashboard |
| `images/`              | Screenshots for preview in README |

---

## 🔗 GitHub Repository

> [View This Project on GitHub](https://github.com/kushitec15691/Olympic-DataEngineering-Project)

---

## 👤 Author

**Kushmi Anuththara**  
*Master's in Data Science | Data Engineer | Azure & Power BI Enthusiast*  
📍 Based in Sweden  
📫 [LinkedIn](https://www.linkedin.com/in/kushmianuththara)

---

## 📄 License

This project is licensed under the MIT License.
