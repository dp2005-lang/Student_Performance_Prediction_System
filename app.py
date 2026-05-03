from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/student_model.joblib")

class Student(BaseModel):
    prior_gpa: float
    attendance_pct: float
    quiz_avg: float
    assign_avg: float
    midterm: float
    study_hours_wk: float
    on_time_submit_pct: float
    lms_logins_wk: float
    forum_posts: int
    commute_min: float
    gender: str
    school_type: str
    parent_edu: str

@app.post("/predict")
def predict(s: Student):
    df = pd.get_dummies(pd.DataFrame([s.dict()]))
    prob = model.predict_proba(df)[0][1]
    return {"risk": round(prob*100, 1), "at_risk": prob < 0.5}
