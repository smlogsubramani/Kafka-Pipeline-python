from kafka import KafkaProducer
import os
 
# Kafka broker address
bootstrap_servers = 'localhost:9092'
# Kafka topic to which messages will be sent
topic = 'audio_topic'
 
# Function to read audio files from a folder
def read_audio_files(folder_path):
    audio_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.ogg'):
            audio_files.append(os.path.join(folder_path, file))
    return audio_files
 
# Function to read audio file as binary data
def read_audio(file_path):
    with open(file_path, 'rb') as f:
        return f.read()
 
# Function to send audio data to Kafka
def send_audio_to_kafka(audio_files, producer):
    for file in audio_files:
        # Read audio file as binary data
        audio_bytes = read_audio(file)
        # Send audio data to Kafka
        producer.send(topic, value=audio_bytes)
        print(f"Sent {file} to Kafka")
 
def main():
    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
 
    # Folder containing audio files
    folder_path ='C:\dataformutipleaudio'
 
    # Read audio files from the folder
    audio_files = read_audio_files(folder_path)
 
    # Send audio files to Kafka
    send_audio_to_kafka(audio_files, producer)
    
    # Close Kafka producer
    producer.close()
 
if __name__ == "__main__":
    main()