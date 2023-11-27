#!/bin/bash

if ! command -v parallel &> /dev/null; then
  echo "GNU Parallel is not installed. Installing..."
  sudo apt-get update
  sudo apt-get install -y parallel
  if [ $? -ne 0 ]; then
    echo "Error: Unable to install GNU Parallel. Please install it manually and rerun the script."
    exit 1
  fi
fi


read -p "Enter path to the directory containing audio files: " input_dir
read -p "Enter path to the output directory: " output_dir
read -p "Enter the number of CPUs to use for parallel processing: " num_cpus


if [ ! -d "$input_dir" ]; then
  echo "Input directory does not exist. Please provide a valid path."
  exit 1
fi

if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
  echo "Created output directory: $output_dir"
fi

export output_dir


find "$input_dir" -type f | parallel -j"$num_cpus" bash -c '
  convert_to_wav() {
    file="$1"
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"
    output_file="$output_dir/$filename_noext.wav"
    ffmpeg -i "$file" -ac 1 -ar 16000 "$output_file"
    echo "Converted $filename to WAV format."
  }

  convert_to_wav {}
'

echo "Conversion complete. All audio files processed and stored in $output_dir."
