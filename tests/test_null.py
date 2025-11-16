from src.load_dataset import load_dataset

def test_null():
    df = load_dataset()
    has_null = df.isnull().values.any()
    assert (not has_null)
   
