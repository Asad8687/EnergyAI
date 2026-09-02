# Koppling mellan EnergyAI och kursmål 1–8

| Kursmål | Hur projektet uppfyller det | Evidens |
|---|---|---|
| 1 | Kafka producer/consumer och eventbaserad behandling | `src/kafka_producer.py`, `src/kafka_consumer.py` |
| 2 | Decision Tree och Random Forest | notebook + `train_models.py` |
| 3 | Keras/TensorFlow MLP | notebook + `train_models.py` |
| 4 | EDA, preprocessing, feature engineering | notebook |
| 5 | Kontinuerlig streaming + anomaly detection | Kafka consumer + Isolation Forest |
| 6 | Kombination av tids-, väder- och inomhussensordata | notebook |
| 7 | Färdig prediktions-/anomalitillämpning och dashboard | `app.py` |
| 8 | Tidsbaserad validering samt streaming-arkitektur/benchmark | notebook + Kafka-loggar |

## Bedömning
Projektet demonstrerar både kunskaper, färdigheter och kompetenser. För högre ambitionsnivå bör metodval, begränsningar, leakage-risker, skalbarhet och modelljämförelser förklaras med de faktiska resultaten från körningen.
