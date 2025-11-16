import pandas as pd

def load_dataset():
    df = pd.read_csv('data/Iris.csv')
    return df


load_dataset()