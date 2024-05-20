import base64
import os
from kafka import KafkaConsumer
import azure.cognitiveservices.speech as speechsdk

# Function to recognize speech from audio file using Azure Cognitive Services
def recognize_from_audio_file(file_path,audio_data):
    try:
        # Write the audio data to the file
        with open(file_path, 'wb') as f:
            f.write(audio_data)
        print(file_path)
        # Set up Azure Cognitive Services speech configuration
        speech_config = speechsdk.SpeechConfig(subscription='79ce5b4cae30453dab96717625554c1d', region='eastus')
        speech_config.speech_recognition_language = "en-US"
        audio_config = speechsdk.audio.AudioConfig(filename=file_path)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        # Perform speech recognition
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
    except Exception as e:
        print(f"Error recognizing speech: {e}")

# Kafka consumer configuration
output_folder = r'C:\testfoldernewaudio'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
 
consumer = KafkaConsumer(
    'audio_topic_multi',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='audio-group'
)
 
# Process messages from Kafka
for message in consumer:
    try:
        # Decode the Base64 string back to audio bytes
        audio_b64 = message.value.decode('utf-8')
        audio_data = base64.b64decode(audio_b64)
 
        file_name = f"audio_{message.offset}.wav"
        file_path = os.path.join(output_folder, file_name)
 
        recognize_from_audio_file(file_path,audio_data)
       
    except Exception as e:
        print(f"Error processing message: {e}")
consumer.close()