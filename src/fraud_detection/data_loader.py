import pandas as pd

def load_data(csv):
    df = pd.read_csv(csv)
    return df

def info_summary(df):
    shape = df.shape
    num_duplicates = df.duplicated().sum()
    
    summary = f"Data Shape: {shape}\nDuplicate Rows: {num_duplicates}"
    
    return summary