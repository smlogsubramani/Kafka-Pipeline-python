from pydub import AudioSegment

def convert_to_wav(audio_file, output_file): 
    # Load audio file
    sound = AudioSegment.from_file(audio_file)
    # Ensure the audio is in WAV format
    if sound.channels != 1:
        sound = sound.set_channels(1)  # Convert stereo to mono
    if sound.frame_rate != 44100:
        sound = sound.set_frame_rate(44100)  # Set frame rate to 44100 Hz
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)  # Set sample width to 16-bit
    # Export as WAV
    sound.export(output_file, format="wav")

# Example usage
input_file = r'C:\testfoldernewaudio\3_testaudio.ogg'  # Note the use of raw string literal
output_file = r'C:\testfoldernewaudio\voice.wav'  # Note the use of raw string literal
convert_to_wav(input_file, output_file)
