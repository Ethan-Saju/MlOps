import pandas as pd

def load_dataset():
    df = pd.read_csv('data/Iris.csv')
    df = df.drop(columns=["Id"])
    return df


load_dataset()