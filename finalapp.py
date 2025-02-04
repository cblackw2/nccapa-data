# finalapp.py
import streamlit as st
import os
from modules import data_module, visualization_module, ai_module, ui_module

# Set page configuration
st.set_page_config(page_title="NC/CAPA Insight Reviewer", layout="wide")

# --- Sidebar: Configuration ---
st.sidebar.title("Configuration")
api_key = ui_module.get_api_key()
if api_key:
    ai_module.initialize_openai(api_key)
else:
    st.sidebar.warning("API key required to generate insight reports.")

report_type = st.sidebar.selectbox("Select Report Type", ("Summary Report", "Deep Dive Analysis"))

# --- Main UI: Data Upload and Display ---
st.title("NC/CAPA Data Review")
st.markdown("Upload your NC/CAPA CSV file for analysis.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
df = None
if uploaded_file is not None:
    try:
        df = data_module.load_data(uploaded_file)
        st.success("Data loaded successfully!")
        st.write("### Data Preview", df.head())
    except Exception as e:
        st.error(f"Error loading data: {e}")
else:
    st.info("Please upload a CSV file containing NC/CAPA data.")

# --- Visualization ---
if df is not None:
    st.write("### Nonconformance Count by Department")
    try:
        fig = visualization_module.department_chart(df)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Visualization error: {e}")

# --- AI Insight Report Generation ---
st.write("### Generate Insight Report")
user_query = st.text_input(
    "Enter your specific question or request for insights:",
    placeholder="E.g., 'What are the main trends in the last quarter?'"
)
if st.button("Generate Report"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif df is None:
        st.error("Please upload NC/CAPA data before generating a report.")
    elif user_query.strip() == "":
        st.error("Please enter a query for the report.")
    else:
        with st.spinner("Generating report..."):
            report = ai_module.generate_insight_report(df, report_type, user_query)
            st.write("### Insight Report")
            st.text_area("Report Output", value=report, height=400)

st.markdown("---")
st.markdown("Developed by your team. © 2025")

