from kafka import KafkaConsumer
import json
 
# Configuration
kafka_topic = "json_topic"
bootstrap_servers = 'localhost:9092'  
group_id = "json_group_id"  


consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=group_id,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
 
def consume_and_process():
    for message in consumer:
        data = message.value
        print(f"Consumed data from topic {kafka_topic}: {data}")

 
if __name__ == "__main__":
    consume_and_process()