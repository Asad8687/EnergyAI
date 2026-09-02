import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from ucimlrepo import fetch_ucirepo

st.set_page_config(page_title="EnergyAI", layout="wide")
st.title("⚡ EnergyAI – Energy Prediction & Anomaly Detection")
st.caption("Reference dashboard for the EnergyAI project")

@st.cache_data
def load_data():
    ds = fetch_ucirepo(id=374)
    df = pd.concat([ds.data.features.copy(), ds.data.targets.copy()], axis=1)
    df["date"] = pd.to_datetime(
    df["date"].astype(str).str.replace(
        r"(\d{4}-\d{2}-\d{2})(\d{2}:)", r"\1 \2", regex=True
    )
)
    return df.sort_values("date")

df = load_data()

c1, c2, c3 = st.columns(3)
c1.metric("Observationer", f"{len(df):,}")
c2.metric("Medel", f"{df.Appliances.mean():.1f} Wh")
c3.metric("Max", f"{df.Appliances.max():.1f} Wh")

fig = px.line(df.tail(1500), x="date", y="Appliances",
              title="Energiförbrukning – senaste observationerna")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Temperatur och energiförbrukning")
fig2 = px.scatter(df.sample(min(4000, len(df)), random_state=42),
                  x="T_out", y="Appliances", opacity=0.35)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Modell")
model_path = Path("models/random_forest.joblib")
if model_path.exists():
    st.success("Random Forest-modellen finns sparad och kan användas av streamingdelen.")
else:
    st.warning("Kör `python src/train_models.py` först för att skapa modellerna.")
