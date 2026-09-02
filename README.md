
1. Dataströmmar/händelsebearbetning → Kafka producer/consumer.
2. Beslutsträd/ensemble → Decision Tree + Random Forest.
3. Deep learning → Keras/TensorFlow MLP.
4. Datautvinning → preprocessing, EDA, feature engineering.
5. Kontinuerlig analys → streaming + anomaly detection.
6. Datautvinning på olika data → energimål + väder/sensorfeatures.
7. ML/DL-tillämpning → prediktions- och anomalitjänst + dashboard.
8. Utvärdering av dataströmsbearbetning → benchmark/loggning och diskussion.

## Dataset
UCI Machine Learning Repository, Appliances Energy Prediction:
https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction

Projektet laddar datasetet automatiskt via `ucimlrepo`.

## Struktur
- `notebooks/energyai_complete.ipynb` – analys, träning, utvärdering och anomaly detection
- `src/train_models.py` – tränar och sparar modeller
- `src/stream_simulator.py` – simulerar sensordata
- `src/kafka_producer.py` – skickar data till Kafka
- `src/kafka_consumer.py` – läser Kafka och gör prediktion/anomalikontroll
- `app.py` – Streamlit-dashboard
- `requirements.txt` – paket
- `docker-compose.yml` – lokal Kafka
- `PROJECT_MAPPING.md` – detaljerad koppling till kursmål

## Snabbstart
1. Installera paketen:
   `pip install -r requirements.txt`
2. Kör notebooken för analys och modellträning.
3. Starta dashboard:
   `streamlit run app.py`
4. Kafka-delen är en valfri lokal realtidsutbyggnad:
   `docker compose up -d`
5. Kör producer och consumer i separata terminaler.


