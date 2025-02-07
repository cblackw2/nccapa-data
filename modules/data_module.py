# modules/data_module.py
import pandas as pd

def load_data(uploaded_file) -> pd.DataFrame:
    """
    Load NC/CAPA data from an Excel file into a pandas DataFrame.
    """
    try:
        # Determine file type based on the file extension
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        raise Exception(f"Error loading file: {e}")
