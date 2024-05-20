from kafka import KafkaProducer
import base64
import os

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_audio_files(file_paths, topic):
    for file_path in file_paths:
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

# Function to get all file paths from a directory
def get_files_in_directory(directory):
    file_paths = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.wav'):  # Adjust file extension as needed
            file_paths.append(os.path.join(directory, file_name))
    return file_paths

# Example usage
directory_path = r'C:\initaltry'
topic = 'audio_topic_multi'
file_paths = get_files_in_directory(directory_path)
send_audio_files(file_paths, topic)
