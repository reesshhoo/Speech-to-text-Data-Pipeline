import os
import requests
import subprocess

course_url = input("Enter the course URL: ")

def extract_course_id(url):
    parts = url.split('/')
    course_id = parts[-1]
    return course_id

course_id = extract_course_id(course_url)

url_for_download = "https://tools.nptel.ac.in/npteldata/downloads.php?id=" + course_id

response = requests.get(url_for_download)

if response.status_code == 200:

    data = response.json()
 
    def download_audio():
        def extract_audio(video_url, output_filename):
            try:
                subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', '{}.%(ext)s'.format(output_filename), video_url], check=True)
                print("Audio downloaded and saved as {}.mp3".format(output_filename))
            except subprocess.CalledProcessError as e:
                print("An error occurred: {}".format(e))

        os.makedirs('audio', exist_ok=True)

        for video_info in data['data']['course_downloads']:
            video_title = video_info['lesson_id']
            video_url = video_info['url']
            extract_audio(video_url, os.path.join('audio', video_title))

    def download_transcript():
        try:
            def extract_transcript_id(drive_link):
                parts = drive_link.split('/')
                transcript_id = parts[-2]
                return transcript_id
            
            def get_direct_download_link(file_id):
                res = requests.get(f'https://drive.google.com/uc?id={file_id}&export=download')
                if res.status_code == 200:
                    download_link = res.url
                    return download_link
                else:
                    return None

            def download_file(url, destination):
                response = requests.get(url)
                if response.status_code == 200:
                    with open(destination, 'wb') as file:
                        file.write(response.content)
                    print(f"File downloaded to {destination}")
                else:
                    print("Failed to download the file")

            os.makedirs('transcripts', exist_ok=True)

            for transcript_info in data['data']['transcripts']:
                transcript_links = transcript_info['downloads']
                for i in transcript_links:
                    if i['language']=='english-Verified':
                        transcript_id = extract_transcript_id(i['url'])
                        direct_download_link = get_direct_download_link(transcript_id)
                        destination_path = os.path.join('transcripts', transcript_info['lesson_id'] + '.pdf')
                        try:
                            download_file(direct_download_link, destination_path)
                        except Exception as e:
                            print(f"Failed to download {destination_path}: {e}")
                            continue
        except Exception as e:
            print(e)
    download_transcript()
    download_audio()
else:
    print("Failed to fetch data from the URL")
