# Speech-to-text-Data-Pipeline

This is a Data Collection and Transformation Pipeline that converts NPTEL lectures into audio files and downloads the transcripts of those lectures.
It's involves pre-processing steps such as changing the format of the downloaded audio files as well as scraping the text from the downloaded pdfs.
The downloaded data is then structured into a jsonl file.

## Instructions to run the Pipeline

- Open your terminal and run `./app.sh`. From this point onwards, the user is only required to enter the path where the files are stored.
- The script will first install all the necessary requirements from requirements.txt.
- The, it will ask for the URL of the course you want the data for. Paste the link of the NPTEL course.
- The downloaded files be stored in `audio` and `transcripts` folders.
- It will then execute the `script.sh` to change the format of the audio files to `.wav` format and with a 16KHz sampling rate, mono channel format.
- The code will parallelize the code N CPUs
- It is to be observed that the last 30 secs of all the lectures are the outro of the elctures and do not contain any speech and is therefore, is of no use. So a `wav_editor.py` will be executed to trim the last 30 secs of all lectures. It will ask for the directory where you have stored the .wav files converted from the downloaded audio files.
- Then we proceed to scrape the text from the downloaded pdf files. `text_scraper.py` will scrape the text from the transcripts' pdf file and store it in the output directory specified by the user.
**Observation**: It was found that approximately the first 150 characters or so in the pdf file are just the heading of the transcripts which does not contribute to our cause because that's not spoken in the audio file. Therefore, we will proceed with removing those characters.
- Lastly, it executes the `manifest.py` which creates a `.jsonl` file. `train_manifest.jsonl` is an example file for one of the nptel courses that is attached in the repo.
