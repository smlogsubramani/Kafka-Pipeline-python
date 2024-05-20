from kafka import KafkaConsumer
import base64
import os
 
# Kafka broker address
bootstrap_servers = 'localhost:9092'
# Kafka topic to receive audio data
topic = 'audio_topic'
# Output folder to save audio files
output_folder = 'C:\output_folder'
 
# Create Kafka Consumer
consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers)
 
def receive_audio():
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    print("file created")
 
    for message in consumer:
        # Decode Base64-encoded audio data
        encoded_audio = message.value
        audio_data = base64.b64decode(encoded_audio)
        print(audio_data,encoded_audio)
        
        # Define the file path to save the audio file
        file_name = f"audio_{message.offset}.ogg"  # You can customize the file naming convention
        file_path = os.path.join(output_folder, file_name)
 
        # Write the audio data to the file
        with open(file_path, 'wb') as f:
            f.write(audio_data)
 
        print(f"Received audio data saved to '{file_path}'")
 
# Example usage
receive_audio()