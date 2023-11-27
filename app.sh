# #!/bin/bash

pip install -r requirements.txt

python downloader.py

if [ $? -ne 0 ]; then
echo "Error: Unable to run downloader.py"
exit 1
fi

chmod +x script.sh
./script.sh

if [ $? -ne 0 ]; then
echo "Error: Unable to convert audio files to .wav"
exit 1
fi

python wav_editor.py

if [ $? -ne 0 ]; then
echo "Error: Unable to execute audio file trimmer"
exit 1
fi

python text_scraper.py

if [ $? -ne 0 ]; then
echo "Error: Couldn't scrape text using text_scraper.py"
exit 1
fi

python manifest.py


if [ $? -ne 0 ]; then
echo "Error: Unable to create jsonl file"
exit 1
fi