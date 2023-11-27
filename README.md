# Speech-to-text-Data-Pipeline

This is a Data Collection and Transformation Pipeline that converts NPTEL lectures into audio files and downloads the transcripts of those lectures.
It's involves pre-processing steps such as changing the format of the downloaded audio files as well as scraping the text from the downloaded pdfs.
The downloaded data is then structured into a jsonl file.

## Instructions to run the Pipeline

- Open your terminal and ron `./app.sh`
- It will ask for the URL of the course you want the data for. Paste the link of the NPTEL course.
