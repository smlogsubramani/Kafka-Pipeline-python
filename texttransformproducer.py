from kafka import KafkaProducer
import base64
import os
 
# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')
 
def send_audio_file(file_path, topic):
    # Read the audio file in binary mode
    with open(file_path, 'rb') as audio_file:
        audio_bytes = audio_file.read()
        
    # Encode the audio bytes in Base64
    audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    # Send the Base64 encoded audio to Kafka
    producer.send(topic, value=audio_b64.encode('utf-8'))
    producer.flush()
    print(f"Sent audio file {file_path} to topic {topic}")

    audio_file.close()
 
# Example usage
file_path = r'C:\initaltry\wavaudio.wav'  
topic = 'audio_topic'  
send_audio_file(file_path, topic)