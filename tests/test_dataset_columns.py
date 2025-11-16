from src.load_dataset import load_dataset

#required columns are there 
def test_dataset_columns():
    df=load_dataset()
    required_columns=['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
    for col in required_columns:
        assert col in df.columns, f"Missing column: {col}"