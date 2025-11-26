from load_dataset import load_dataset
from sklearn.model_selection import train_test_split   
from sklearn.preprocessing import LabelEncoder        
from sklearn.metrics import accuracy_score, classification_report  
from models import models 
import json 


df = load_dataset()

X = df.drop("Species", axis=1)                        
y = df["Species"]   

le = LabelEncoder()
y = le.fit_transform(y) 

TEST_SIZE = 0.2
RANDOM_STATE = 42


X_train, X_test, y_train, y_test = train_test_split(  
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

best_model = dict()


results = []


for model in models:

    model_name = model.__class__.__name__

    print(f"\nTraining Model: {model_name}")

    model.fit(X_train, y_train)     

    y_pred = model.predict(X_test)                          

    accuracy = accuracy_score(y_test, y_pred)

    report = classification_report(y_test, y_pred, output_dict=True)

    precision = report["weighted avg"]["precision"]
    recall = report["weighted avg"]["recall"]
    f1 = report["weighted avg"]["f1-score"]

    current_model = {
        "model": model,
        "model_name": model_name,
        "accuracy": accuracy
    }

    if (not best_model) or (accuracy > best_model["accuracy"]):
        best_model = current_model

    model_result = {
        "model_name": model_name,
        "metrics": {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }
    }

    results.append(model_result)

with open("src/model_results.json", "w") as f:
    json.dump(results, f, indent=4)

with open("src/best_model_info.json", "w") as f:
    json.dump({
        "model_name": best_model["model_name"],
        "accuracy": best_model["accuracy"]
    }, f, indent=4)

import pickle

with open("src/best_model.pkl", "wb") as f:
    pickle.dump(best_model["model"], f)

with open("src/label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)
