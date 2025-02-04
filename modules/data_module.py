# modules/data_module.py
import pandas as pd

def load_data(uploaded_file) -> pd.DataFrame:
    """
    Load NC/CAPA data from a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")
