YouTube Video Downloader (Backend API)
This is a Python-based Flask application that serves as a backend API for a YouTube video downloader. It uses the yt-dlp library to fetch video information and download videos based on user requests.

Features
API-driven: Exposes RESTful API endpoints for interaction.

Video Information: The /formats endpoint allows you to retrieve a list of all available video and audio formats for a given YouTube URL.

Video Download: The /download endpoint initiates the video download to the server, supporting specific formats or a target resolution (e.g., 720p).

File Serving: The /download_file endpoint serves the downloaded video file to the client.

Requirements
To run this application, you need to have Python 3.x and the following libraries installed:

Flask

yt-dlp

Setup and Installation
Save your Flask code as a file named app.py.

Open your terminal or command prompt.

Install the required Python packages using pip:

pip install Flask yt-dlp

Run the Flask application by executing the script:

python app.py

The server will start and be accessible at http://127.0.0.1:5000. It will also automatically create a downloads folder to store the videos.

API Endpoints
This application exposes three main API endpoints that you can call with tools like cURL or Postman.

1. Get Available Formats (/formats)
   Method: POST

Description: Retrieves a list of all available formats and resolutions for a video.

Request Body (JSON):

{
"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

2. Download Video (/download)
   Method: POST

Description: Downloads the video to the server. You can specify a format_id or a resolution. If neither is provided, it downloads the best available quality.

Request Body (JSON):

{
"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
"resolution": 720
}

Example cURL Command:

curl -X POST \
 -H "Content-Type: application/json" \
 -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "resolution": 720}' \
 http://127.0.0.1:5000/download

3. Download File (/download_file)
   Method: GET

Description: Serves the downloaded file to the client. This endpoint is meant to be called after a successful download, using the file_path returned from the /download endpoint.

Request Parameters: file_path (string)

Example cURL Command:

curl -o "video.mp4" "http://127.0.0.1:5000/download_file?file_path=downloads%2FA_Downloaded_Video.mp4"
