from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load("src/best_model.pkl")

le = joblib.load("src/label_encoder.pkl")

app = FastAPI(title="Iris Species Predictor")


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/api/predict")
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
        "test": "test",
        "hello world":"hello",
        "test2":"test2"
    }
