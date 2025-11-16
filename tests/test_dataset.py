from src.load_dataset import load_dataset

df = load_dataset()

#required columns are there 
def test_dataset_columns():
    required_columns=['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
    for col in required_columns:
        assert col in df.columns, f"Missing column: {col}"
def test_null_values():
    has_null = df.isnull().values.any()
    assert (not has_null)
   
def test_no_duplicates():
    assert df.duplicated().sum() == 0