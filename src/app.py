from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("src/best_model.pkl")

le = joblib.load("src/label_encoder.pkl")

app = FastAPI(title="Iris Species Predictor")


# Request body model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict_species(data: IrisInput):
 
    input_array = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = model.predict(input_array)[0]   


    species = le.inverse_transform([prediction])[0]

    return {
        "prediction": str(species),
        "test": "test"
        "hello world"
    }
