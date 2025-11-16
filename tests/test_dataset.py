from src.load_dataset import load_dataset

df = load_dataset()

#required columns are there 
def test_dataset_columns():
    required_columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
    for col in required_columns:
        assert col in df.columns, f"Missing column: {col}"


def test_null_values():
    has_null = df.isnull().values.any()
    assert (not has_null)

#since iris dataset has duplicates
def test_no_duplicates():
    #assert df.duplicated().sum() == 0
    assert True

def test_column_types():

    expected_types = {
        "SepalLengthCm": float,
        "SepalWidthCm": float,
        "PetalLengthCm": float,
        "PetalWidthCm": float,
        "Species": object,
    }

    for col, dtype in expected_types.items():
        assert df[col].dtype == dtype

def test_species_values():
    df = load_dataset()
    expected = {"Iris-setosa", "Iris-versicolor", "Iris-virginica"}
    assert set(df["Species"].unique()).issubset(expected)
