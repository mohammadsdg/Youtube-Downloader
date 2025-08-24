from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def is_valid_youtube_url(url):
    return "youtube.com/watch" in url or "youtu.be/" in url

@app.route('/formats', methods=['POST'])
def get_formats():
    """
    Get all available formats for a YouTube video.
    """
    try:
        data = request.get_json(force=True)
        url = data.get('url')
        if not url:
            return jsonify({"error": "Missing 'url' parameter."}), 400
        if not is_valid_youtube_url(url):
            return jsonify({"error": "Invalid YouTube URL."}), 400

        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = []
            for f in info['formats']:
                formats.append({
                    "format_id": f.get('format_id'),
                    "ext": f.get('ext'),
                    "resolution": f.get('height'),
                    "fps": f.get('fps'),
                    "note": f.get('format_note'),
                    "url": f.get('url')
                })
        return jsonify({"title": info.get('title'), "formats": formats}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download', methods=['POST'])
def download_video():
    """
    Download a video from YouTube.
    JSON body can include:
    - url: YouTube URL (required)
    - format_id: optional, to download a specific format
    - resolution: optional, max resolution if format_id not provided
    """
    try:
        data = request.get_json(force=True)
        url = data.get('url')
        format_id = data.get('format_id')
        resolution = data.get('resolution')  # integer, e.g., 720

        if not url:
            return jsonify({"error": "Missing 'url' parameter."}), 400
        if not is_valid_youtube_url(url):
            return jsonify({"error": "Invalid YouTube URL."}), 400

        # Build yt-dlp format string
        if format_id:
            format_str = format_id
        elif resolution:
            format_str = f"bestvideo[height<={resolution}]+bestaudio/best"
        else:
            format_str = "best"

        ydl_opts = {
            'format': format_str,
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return jsonify({
            "message": "Video downloaded successfully",
            "file_path": filename
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download_file', methods=['GET'])
def download_file():
    """
    Serve a downloaded video file to the client.
    """
    try:
        file_path = request.args.get('file_path')
        if not file_path or not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
