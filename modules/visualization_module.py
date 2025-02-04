# modules/visualization_module.py
import plotly.express as px
import pandas as pd

def department_chart(df: pd.DataFrame):
    """
    Create a bar chart showing nonconformance counts by department.
    Expects a column named 'Department' in the DataFrame.
    """
    if "Department" in df.columns:
        dept_counts = df["Department"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Count"]
        fig = px.bar(dept_counts, x="Department", y="Count", title="Nonconformance Count by Department")
        return fig
    else:
        raise Exception("Column 'Department' not found in data.")

