# YouTube-Downloader

A Python-based backend API for downloading YouTube videos, built using Flask and yt-dlp.

## 🚀 Features

- **API-Driven**: Exposes RESTful API endpoints for interaction.
- **Video Information**: Retrieve a list of all available video and audio formats for a given YouTube URL.
- **Video Download**: Initiate video downloads to the server, supporting specific formats or target resolutions (e.g., 720p).
- **File Serving**: Serve the downloaded video file to the client.

## 📦 Requirements

To run this application, ensure you have Python 3.x installed, along with the following libraries:

- `Flask`
- `yt-dlp`

You can install them using pip:

```bash
pip install Flask yt-dlp
```

## ⚙️ Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammadsdg/Youtube-Downloader.git
   cd Youtube-Downloader
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

The application will start running on `http://127.0.0.1:5000/`.

## 🧪 API Endpoints

### `GET /formats`

Retrieve a list of all available video and audio formats for a given YouTube URL.

**Parameters:**

- `url` (required): The YouTube video URL.

**Example Request:**

```bash
curl "http://127.0.0.1:5000/formats?url=https://www.youtube.com/watch?v=example"
```

**Response:**

```json
{
  "formats": [
    {
      "format": "22",
      "resolution": "720p",
      "extension": "mp4",
      "audio": true,
      "video": true
    },
    {
      "format": "18",
      "resolution": "360p",
      "extension": "mp4",
      "audio": true,
      "video": true
    }
  ]
}
```

### `GET /download`

Initiate the download of a video.

**Parameters:**

- `url` (required): The YouTube video URL.
- `format` (optional): The desired format ID.
- `resolution` (optional): The desired resolution (e.g., `720p`).

**Example Request:**

```bash
curl "http://127.0.0.1:5000/download?url=https://www.youtube.com/watch?v=example&resolution=720p"
```

**Response:**

```json
{
  "message": "Download started successfully."
}
```

### `GET /download_file`

Serve the downloaded video file to the client.

**Parameters:**

- `filename` (required): The name of the downloaded file.

**Example Request:**

```bash
curl "http://127.0.0.1:5000/download_file?filename=example_video.mp4" --output example_video.mp4
```

**Response:**
The video file will be downloaded to the client's machine.

## 🧩 Example Usage

1. Use the `/formats` endpoint to check available formats for a video:

   ```bash
   curl "http://127.0.0.1:5000/formats?url=https://www.youtube.com/watch?v=example"
   ```

2. Choose a desired format and resolution.

3. Use the `/download` endpoint to start the download:

   ```bash
   curl "http://127.0.0.1:5000/download?url=https://www.youtube.com/watch?v=example&resolution=720p"
   ```

4. Once the download is complete, use the `/download_file` endpoint to retrieve the video:

   ```bash
   curl "http://127.0.0.1:5000/download_file?filename=example_video.mp4" --output example_video.mp4
   ```

## 🛠️ Development & Contributions

Feel free to fork the repository, submit issues, and send pull requests. Contributions are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
