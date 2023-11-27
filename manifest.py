import os
import wave
import json

def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as audio_file:
        frame_rate = audio_file.getframerate()
        num_frames = audio_file.getnframes()
        duration = float(num_frames) / frame_rate
        return round(duration, 2)


audio_folder = input('Enter the path containing the audio files: ')
text_folder = input('Enter the path containing the text files: ')
output_manifest_file = 'train_manifest.jsonl'

with open(output_manifest_file, 'w') as manifest:
    for filename in os.listdir(audio_folder):
        if filename.endswith('.wav'):
            audio_filepath = os.path.join(audio_folder, filename)
            audio_id = os.path.splitext(filename)[0]
            text_filepath = os.path.join(text_folder, f'{audio_id}.txt')

            if os.path.exists(text_filepath):
                with open(text_filepath, 'r') as text_file:
                    text = text_file.read().strip()

                duration = get_wav_duration(audio_filepath)

                manifest_line = {
                    'audio_filepath': audio_filepath,
                    'duration': duration,
                    'text': text
                }

                manifest.write(json.dumps(manifest_line) + '\n')
