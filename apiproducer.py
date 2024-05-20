from kafka import KafkaProducer
import requests
import json
import time
 

api_url = "https://api.sampleapis.com/switch/games"  
kafka_topic = "json_topic"
bootstrap_servers = 'localhost:9092' 
 

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
 
def fetch_and_produce():
    while True:
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
 
            # Produce data to Kafka topic
            producer.send(kafka_topic, value=data)
            producer.flush()
 
            print(f"Produced data to topic {kafka_topic}: {data}")
 
            # Wait before fetching new data
            time.sleep(60)  
 
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            time.sleep(60)  # Wait before retrying
 
if __name__ == "__main__":
    fetch_and_produce()

