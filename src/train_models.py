from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

OUT = Path("models")
OUT.mkdir(exist_ok=True)

dataset = fetch_ucirepo(id=374)
df = pd.concat([dataset.data.features.copy(), dataset.data.targets.copy()], axis=1)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

df["hour"] = df.date.dt.hour
df["dayofweek"] = df.date.dt.dayofweek
df["month"] = df.date.dt.month
df["is_weekend"] = (df.dayofweek >= 5).astype(int)
df["lag_1"] = df.Appliances.shift(1)
df["lag_6"] = df.Appliances.shift(6)
df["lag_144"] = df.Appliances.shift(144)
df = df.dropna().reset_index(drop=True)

features = [
    "lights","T1","RH_1","T2","RH_2","T3","RH_3","T4","RH_4","T5","RH_5",
    "T6","RH_6","T7","RH_7","T8","RH_8","T9","RH_9","T_out","Press_mm_hg",
    "RH_out","Windspeed","Visibility","Tdewpoint","hour","dayofweek","month",
    "is_weekend","lag_1","lag_6","lag_144"
]
X, y = df[features], df["Appliances"]
split = int(len(df)*0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

models = {
    "linear_regression": Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())]),
    "decision_tree": DecisionTreeRegressor(max_depth=12, random_state=42),
    "random_forest": RandomForestRegressor(n_estimators=200, max_depth=18, random_state=42, n_jobs=-1)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, OUT/f"{name}.joblib")

iso = IsolationForest(n_estimators=200, contamination=0.02, random_state=42)
iso.fit(df[["Appliances","T_out","RH_out","Windspeed","hour","dayofweek"]])
joblib.dump(iso, OUT/"isolation_forest.joblib")

joblib.dump(features, OUT/"features.joblib")
print("Models saved to ./models")
