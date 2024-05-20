from kafka import KafkaConsumer
import os
 
# Kafka broker address
bootstrap_servers = 'localhost:9092'
# Kafka topic from which messages will be consumed
topic = 'audio_topic'
# Directory to save received audio files

output_dir = 'C:\outputformutipleaudio'
 
# Function to save audio data to file
def save_audio_file(file_name, audio_data):
    with open(file_name, 'wb') as f:
        f.write(audio_data)
    print(f"Saved {file_name}")
 
def main():
    # Initialize Kafka consumer
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='latest')
 
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
 
    # Continuously consume messages from Kafka
    for message in consumer:
        # Construct file name
        file_name = os.path.join(output_dir, f"audio_{message.offset}.ogg")
        # Save audio data to file
        save_audio_file(file_name, message.value)
 
    # Close Kafka consumer
    consumer.close()
 
if __name__ == "__main__":
    main()

