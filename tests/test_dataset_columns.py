from src.load_dataset import load_dataset

#required columns are there 
def test_dataset_columns():
    df=load_dataset()
    required_columns=["sepal_length","sepal_width","petal_length", "petal_width", "species"]
    for col in required_columns:
        assert col in df.columns, f"Missing column: {col}"