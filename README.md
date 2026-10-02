# 🦠 Corona Virus Pandemic Dashboard

**Developed by:** **Yanaguntikar Meesal**


**📧 Email:** **[yanaguntikarm@gmail.com](mailto:yanaguntikarm@gmail.com)**


**🌐 Live Project:** [Open Corona Virus Pandemic Dashboard](https://covid-19-rvuykves6gfgmsjvm73rcq.streamlit.app/)

---

## 📌 Project Overview

The **Corona Virus Pandemic Dashboard** is an interactive data visualization project built using **Python, Streamlit, Pandas, and Plotly**.

The dashboard analyzes COVID-19 pandemic data and provides an easy-to-understand visual representation of:

* 🦠 Total COVID-19 cases
* 🏥 Active/Hospitalized cases
* 💚 Recovered cases
* ⚠️ Deceased cases
* 📍 State-wise COVID-19 cases
* 📊 COVID-19 status distribution
* 📦 Commodity distribution such as Mask, Sanitizer, and Oxygen
* 📋 Complete COVID-19 dataset

The project converts raw COVID-19 data into an interactive dashboard that helps users explore pandemic-related information.

---

## 👨‍💻 Developer

**Name:** Yanaguntikar Meesal
**Email:** [yanaguntikarm@gmail.com](mailto:yanaguntikarm@gmail.com)

This project was developed as a practical **Data Science and Data Visualization project** using Python-based technologies.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Analyze COVID-19 pandemic data.
2. Calculate important COVID-19 statistics.
3. Visualize COVID-19 cases using interactive charts.
4. Compare COVID-19 cases across different states.
5. Analyze the distribution of COVID-related commodities.
6. Create an easy-to-use interactive dashboard using Streamlit.
7. Practice Python data analysis and data visualization skills.

---

## 🛠️ Technologies Used

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Programming language      |
| Streamlit            | Web dashboard             |
| Pandas               | Data loading and analysis |
| Plotly Express       | Interactive charts        |
| Plotly Graph Objects | Customized charts         |
| CSV                  | Dataset format            |

---

## 📁 Project Structure

```text
Corona-Virus-Dashboard/
│
├── app.py
├── corona.csv
└── README.md
```

### `app.py`

Contains the complete Streamlit dashboard application.

### `corona.csv`

Contains the COVID-19 dataset used by the dashboard.

### `README.md`

Contains project documentation and setup instructions.

---

## 📊 Dashboard Features

### 1. KPI Cards

The dashboard displays four important summary statistics:

#### 🦠 Total Cases

Total number of COVID-19 cases.

#### 🏥 Active Cases

Total hospitalized/active cases.

#### 💚 Recovered Cases

Total number of recovered patients.

#### ⚠️ Total Deaths

Total number of deceased patients.

---

## 📦 2. Commodity Analysis

The dashboard provides a commodity analysis section.

Users can select:

* All
* Mask
* Sanitizer
* Oxygen

The selected commodity is visualized according to COVID-19 status.

This helps understand the distribution of important pandemic-related resources.

---

## 📊 3. Zone / Status Distribution

An interactive pie chart allows users to analyze COVID-19 cases based on:

* Status
* State

The chart provides an easy visual comparison of case distribution.

---

## 📍 4. State-wise COVID-19 Analysis

The dashboard provides a state-wise bar chart.

Users can select:

* All
* Hospitalized
* Recovered
* Deceased

The chart then displays the selected case type for every state.

---

## 📋 5. COVID-19 Data Table

The complete dataset is displayed inside an interactive Streamlit data table.

Users can:

* View records
* Scroll through the data
* Examine individual states
* Analyze COVID-19 statistics

---

## 📂 Dataset Requirements

The `corona.csv` file should contain the following columns:

```text
State
Total
Hospitalized
Recovered
Deceased
Status
Mask
Sanitizer
Oxygen
```

Example:

| State       | Total | Hospitalized | Recovered | Deceased | Status    | Mask | Sanitizer | Oxygen |
| ----------- | ----: | -----------: | --------: | -------: | --------- | ---: | --------: | -----: |
| Karnataka   |  1000 |          400 |       550 |       50 | Confirmed |  500 |       300 |    200 |
| Maharashtra |  1500 |          600 |       800 |      100 | Confirmed |  700 |       400 |    300 |
| Delhi       |   900 |          350 |       500 |       50 | Confirmed |  400 |       250 |    150 |

> **Note:** The actual dataset can contain more rows and different values.

---

## 🔄 Project Workflow

```text
                COVID-19 CSV Dataset
                         ↓
                     Pandas
                         ↓
                  Data Loading
                         ↓
                 Data Validation
                         ↓
                 Data Aggregation
                         ↓
          ┌──────────────┴──────────────┐
          ↓                             ↓
    KPI Calculation              State Analysis
          ↓                             ↓
 Total / Active                   Bar Charts
 Recovered / Deaths
          ↓                             ↓
          └──────────────┬──────────────┘
                         ↓
                  Plotly Charts
                         ↓
                  Streamlit UI
                         ↓
              Interactive Dashboard
```

---

## 🚀 Installation

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python:

```bash
python --version
```

---

## 📦 Step 2: Install Required Libraries

Open the VS Code terminal inside your project folder.

Run:

```bash
pip install streamlit pandas plotly
```

---

## ▶️ Step 3: Run the Dashboard

Run:

```bash
streamlit run app.py
```

If the command does not work, use:

```bash
python -m streamlit run app.py
```

The Streamlit dashboard will open in your web browser.

---

## ⚠️ Common Error

### `corona.csv file not found`

If you see:

```text
corona.csv file not found
```

make sure your folder looks like:

```text
Corona-Virus-Dashboard/
│
├── app.py
├── corona.csv
└── README.md
```

The `corona.csv` file must be in the **same folder as `app.py`**.

---

## 💡 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python programming
* Pandas
* CSV data handling
* Data cleaning and validation
* Data aggregation
* GroupBy operations
* Data visualization
* Interactive Plotly charts
* Streamlit
* Dashboard development
* KPI creation
* User input controls
* Data presentation

---

## 💼 Project Summary for Resume

### Corona Virus Pandemic Dashboard

Developed an interactive COVID-19 data analysis dashboard using **Python, Streamlit, Pandas, and Plotly**. Analyzed total, active, recovered, and deceased cases and created interactive state-wise and status-wise visualizations. Implemented KPI cards, commodity analysis for masks, sanitizers and oxygen, interactive pie and bar charts, and a complete dataset view to provide an easy-to-understand representation of pandemic data.

---

## 🎤 Interview Explanation

If an interviewer asks **"Explain your project"**, you can say:

> I developed a Corona Virus Pandemic Dashboard using Python, Streamlit, Pandas, and Plotly. I used a CSV dataset containing state-wise COVID-19 information such as total cases, hospitalized cases, recovered cases, deceased cases, and pandemic-related commodities. I used Pandas for data loading, validation, aggregation, and calculations. I then created KPI cards and interactive Plotly visualizations to analyze cases by status and state. Finally, I used Streamlit to build an interactive web dashboard where users can select different case types and explore the dataset.

---

## 🎯 Future Improvements

The project can be further enhanced by adding:

* 📅 Date-wise COVID-19 trends
* 🗺️ India COVID-19 map
* 📈 Time-series analysis
* 🔎 Search and filtering
* 📊 More interactive charts
* 📥 CSV download button
* 📱 Mobile-friendly dashboard
* 🌎 Country-wise COVID-19 comparison
* 📌 State selection filter
* 📈 Recovery and mortality rates

---

## 🏃 How to Run

```bash
cd Corona-Virus-Dashboard
```

Install libraries:

```bash
pip install streamlit pandas plotly
```

Run application:

```bash
streamlit run app.py
```

---

## 🏆 Project Result

The final result is an interactive **Corona Virus Pandemic Dashboard** that transforms COVID-19 data into meaningful visual insights using Python and modern data visualization tools.

---

## ⭐ Project Technologies

```text
Python
   ↓
Pandas
   ↓
Data Analysis
   ↓
Plotly
   ↓
Interactive Visualization
   ↓
Streamlit
   ↓
COVID-19 Dashboard
```

---

## 👨‍💻 Author

**Yanaguntikar Meesal**

📧 **Email:** [yanaguntikarm@gmail.com](mailto:yanaguntikarm@gmail.com)

🌐 **Live Project:** https://covid-19-rvuykves6gfgmsjvm73rcq.streamlit.app/

---

### 📌 Developer Information

**Developed by Yanaguntikar Meesal**
**Data Science | Python | Pandas | Plotly | Streamlit**

If you have questions or suggestions regarding this project, you can contact me at **[yanaguntikarm@gmail.com](mailto:yanaguntikarm@gmail.com)**.
