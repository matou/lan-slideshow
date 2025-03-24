# LAN Image Slideshow Viewer

A simple web-based slideshow viewer that automatically updates when images are added or removed from a folder.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `media` folder in the same directory as `server.py` (it will be created automatically when you run the server)

4. Place your images in the `media` folder. Supported formats: PNG, JPG, JPEG, GIF, WEBP

## Running the Server

1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt)

2. Start the server:
```bash
python server.py
```

3. The server will start on `http://0.0.0.0:5000`

4. Access the slideshow from any device on your local network by opening a web browser and navigating to:
   - `http://<your-computer-ip>:5000`
   - Replace `<your-computer-ip>` with your computer's local IP address

## Features

- Real-time updates when images are added or removed
- Responsive design that works on all screen sizes
- Navigation buttons to move between images
- Image counter showing current position
- Supports common image formats (PNG, JPG, JPEG, GIF, WEBP) 