import pandas as pd

def load_dataset():
    df = pd.read_csv('../data/iris.csv')
    # print(df.head())
    # print(df.columns)
    # for column in df.columns:
    #     print(column)
    return df

