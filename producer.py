from kafka import KafkaProducer
import base64
import os
 
# Kafka broker address
bootstrap_servers = 'localhost:9092'
# Kafka topic to send audio data
topic = 'audio_topic'
 
# Create Kafka Producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
 
def send_audio(audio_file):
    print("start data")
    # Read audio file as bytes
    with open(audio_file, 'rb') as f:
        audio_data = f.read()
 
    # Encode audio data as Base64
    encoded_audio = base64.b64encode(audio_data)
 
    # Send encoded audio data to Kafka topic
    producer.send(topic, value=encoded_audio)
 
    print(f"Audio file '{audio_file}' sent to Kafka topic '{topic}'")
    print(audio_data,encoded_audio)
 
# Example usage
audio_file_path = r'C:\dataforaudio\testaudio.ogg'
send_audio(audio_file_path)