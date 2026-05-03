import joblib
import pandas as pd

def predict(data):
    model = joblib.load("models/student_model.joblib")
    df = pd.DataFrame([data])
    prob = model.predict_proba(df)[0][1]
    return prob
