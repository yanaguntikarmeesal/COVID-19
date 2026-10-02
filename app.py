

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Corona Virus Pandemic Dashboard",
    page_icon="🦠",
    layout="wide"
)


# =========================================================
# 2. CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: white;
    background: linear-gradient(90deg, #d32f2f, #7b1fa2);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 25px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    margin-bottom: 10px;
}

.total {
    background-color: #dc3545;
}

.active {
    background-color: #17a2b8;
}

.recovered {
    background-color: #ffc107;
    color: black;
}

.deaths {
    background-color: #28a745;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD DATASET
# =========================================================

try:
    patients = pd.read_csv("corona.csv")
except FileNotFoundError:
    st.error("❌ corona.csv file not found.")
    st.info("Please keep corona.csv in the same folder as app.py.")
    st.stop()


# =========================================================
# 4. CHECK REQUIRED COLUMNS
# =========================================================

required_columns = [
    "State",
    "Total",
    "Hospitalized",
    "Recovered",
    "Deceased",
    "Status",
    "Mask",
    "Sanitizer",
    "Oxygen"
]

missing_columns = [
    col for col in required_columns
    if col not in patients.columns
]

if missing_columns:
    st.error("Missing columns in corona.csv:")
    st.write(missing_columns)
    st.stop()


# =========================================================
# 5. CALCULATE SUMMARY
# =========================================================

total = patients["Total"].sum()

active = patients["Hospitalized"].sum()

recovered = patients["Recovered"].sum()

deaths = patients["Deceased"].sum()


# =========================================================
# 6. DASHBOARD TITLE
# =========================================================

st.markdown("""
<div class="title">
    <h1>🦠 Corona Virus Pandemic Dashboard</h1>
    <p>COVID-19 Data Analysis Dashboard</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 7. KPI CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown(f"""
    <div class="card total">
        <h3>Total Cases</h3>
        <h2>{total:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
    <div class="card active">
        <h3>Active Cases</h3>
        <h2>{active:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown(f"""
    <div class="card recovered">
        <h3>Recovered Cases</h3>
        <h2>{recovered:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown(f"""
    <div class="card deaths">
        <h3>Total Deaths</h3>
        <h2>{deaths:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


# =========================================================
# 8. FIRST GRAPH
# Commodity Analysis
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("📦 Commodity Analysis")

    commodity = st.selectbox(
        "Select Commodity",
        [
            "All",
            "Mask",
            "Sanitizer",
            "Oxygen"
        ]
    )

    if commodity == "All":

        fig1 = go.Figure()

        fig1.add_trace(
            go.Bar(
                x=patients["Status"],
                y=patients["Total"],
                name="Total"
            )
        )

        fig1.update_layout(
            title="Total COVID Cases by Status",
            xaxis_title="Status",
            yaxis_title="Cases"
        )

    else:

        fig1 = go.Figure()

        fig1.add_trace(
            go.Bar(
                x=patients["Status"],
                y=patients[commodity],
                name=commodity
            )
        )

        fig1.update_layout(
            title=f"{commodity} Distribution",
            xaxis_title="Status",
            yaxis_title="Count"
        )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )


# =========================================================
# 9. SECOND GRAPH
# Zone / Status Pie Chart
# =========================================================

with col2:

    st.subheader("📊 Zone / Status Distribution")

    zone = st.selectbox(
        "Select Zone",
        [
            "Status",
            "State"
        ]
    )

    if zone == "Status":

        fig2 = px.pie(
            patients,
            names="Status",
            values="Total",
            hole=0.3,
            title="COVID Cases by Status"
        )

    else:

        fig2 = px.pie(
            patients,
            names="State",
            values="Total",
            hole=0.3,
            title="COVID Cases by State"
        )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# =========================================================
# 10. STATE-WISE BAR CHART
# =========================================================

st.markdown("---")

st.subheader("📍 State-wise COVID Cases")


state_type = st.selectbox(
    "Select Case Type",
    [
        "All",
        "Hospitalized",
        "Recovered",
        "Deceased"
    ]
)


if state_type == "All":

    y_column = "Total"

elif state_type == "Hospitalized":

    y_column = "Hospitalized"

elif state_type == "Recovered":

    y_column = "Recovered"

else:

    y_column = "Deceased"


# Group by State
state_data = (
    patients
    .groupby("State")[y_column]
    .sum()
    .reset_index()
)


fig3 = px.bar(
    state_data,
    x="State",
    y=y_column,
    title=f"{state_type} Cases by State",
    text_auto=True
)


fig3.update_layout(
    xaxis_title="State",
    yaxis_title="Number of Cases"
)


st.plotly_chart(
    fig3,
    use_container_width=True
)


# =========================================================
# 11. DATA TABLE
# =========================================================

st.markdown("---")

st.subheader("📋 COVID-19 Dataset")

st.dataframe(
    patients,
    use_container_width=True
)


# =========================================================
# 12. FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<center>

### 🦠 Corona Virus Pandemic Dashboard

Built using **Python + Streamlit + Pandas + Plotly**

</center>
""", unsafe_allow_html=True)

# Install libraries pip install streamlit pandas plotly

# To run the app, use the command: streamlit run app.py
