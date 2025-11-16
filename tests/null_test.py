from src.load_dataset import load_dataset

def test_null():
    df = load_dataset();
    res = (df.isnull().values.any())
    print(res)
    assert(res)

