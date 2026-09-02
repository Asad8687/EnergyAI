import json, time
from kafka import KafkaProducer
from stream_simulator import rows

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "energy-events"
for item in rows():
    producer.send(topic, item)
    producer.flush()
    print("sent:", item["date"], item["Appliances"])
    time.sleep(1)
