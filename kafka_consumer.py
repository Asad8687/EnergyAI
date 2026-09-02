import json, joblib, numpy as np, pandas as pd
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "energy-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

model = joblib.load("models/random_forest.joblib")
features = joblib.load("models/features.joblib")
iso = joblib.load("models/isolation_forest.joblib")

history = []

for msg in consumer:
    d = msg.value
    ts = pd.Timestamp(d["date"])
    history.append(d["Appliances"])

    d["hour"] = ts.hour
    d["dayofweek"] = ts.dayofweek
    d["month"] = ts.month
    d["is_weekend"] = int(ts.dayofweek >= 5)
    d["lag_1"] = history[-2] if len(history) >= 2 else d["Appliances"]
    d["lag_6"] = history[-7] if len(history) >= 7 else d["Appliances"]
    d["lag_144"] = history[-145] if len(history) >= 145 else d["Appliances"]

    X = pd.DataFrame([[d[f] for f in features]], columns=features)
    prediction = float(model.predict(X)[0])

    af = pd.DataFrame([[
        d["Appliances"], d["T_out"], d["RH_out"], d["Windspeed"],
        d["hour"], d["dayofweek"]
    ]], columns=["Appliances","T_out","RH_out","Windspeed","hour","dayofweek"])

    anomaly = int(iso.predict(af)[0]) == -1
    print({
        "timestamp": d["date"],
        "actual_wh": d["Appliances"],
        "predicted_wh": round(prediction, 2),
        "anomaly": anomaly
    }, flush=True)
