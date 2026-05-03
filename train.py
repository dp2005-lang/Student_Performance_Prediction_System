import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/student_data.csv")
X = pd.get_dummies(df.drop(["passed","final_score"], axis=1))
y = df["passed"]
model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, "models/model.pkl")
