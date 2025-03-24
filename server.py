import os
from flask import Flask, send_from_directory, jsonify
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configuration
MEDIA_FOLDER = 'media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Ensure media folder exists
os.makedirs(MEDIA_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_media_files():
    files = []
    for filename in os.listdir(MEDIA_FOLDER):
        if allowed_file(filename):
            files.append(filename)
    return sorted(files)

class MediaFolderHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        if allowed_file(event.src_path.split('/')[-1]):
            time.sleep(0.5)  # Wait for file operations to complete
            socketio.emit('media_update', {'files': get_media_files()})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

@app.route('/api/media')
def get_media():
    return jsonify({'files': get_media_files()})

if __name__ == '__main__':
    # Set up file system observer
    event_handler = MediaFolderHandler()
    observer = Observer()
    observer.schedule(event_handler, MEDIA_FOLDER, recursive=False)
    observer.start()
    
    # Start the server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 