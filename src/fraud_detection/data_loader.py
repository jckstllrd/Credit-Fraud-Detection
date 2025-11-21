import pandas as pd

def load_data(csv):
    df = pd.read_csv(csv)
    print(csv)
    return df