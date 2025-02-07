# modules/visualization_module.py
import plotly.express as px
import pandas as pd

def Site_chart(df: pd.DataFrame):
    """
    Create a bar chart showing nonconformance counts by Site.
    Expects a column named 'Site' in the DataFrame.
    """
    if "Site" in df.columns:
        dept_counts = df["Site"].value_counts().reset_index()
        dept_counts.columns = ["Site", "Count"]
        fig = px.bar(dept_counts, x="Site", y="Count", title="Nonconformance Count by Site")
        return fig
    else:
        raise Exception("Column 'Site' not found in data.")