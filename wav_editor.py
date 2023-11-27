from pydub import AudioSegment
import os

def cut_last_30_seconds(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            file_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            audio = AudioSegment.from_wav(file_path)
            trimmed_audio = audio[:-30000] 
            trimmed_audio.export(output_path, format="wav")


            print(f"Trimmed {file_name} and saved to {output_path}")


input_directory = input("Enter the path of the directory storing wav files: ")
output_directory = input_directory
cut_last_30_seconds(input_directory, output_directory)

