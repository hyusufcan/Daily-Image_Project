#!/usr/bin/env python3
"""
Development Server for The Daily Antiquarian

Serves the website with mock data for local testing
and provides endpoints for simulating API calls.

Usage:
    python dev_server.py
    
Then visit: http://localhost:5000/
"""

from flask import Flask, jsonify, send_from_directory, render_template_string
from pathlib import Path
import json
import os

app = Flask(__name__)

# Static files directory
PUBLIC_DIR = Path(__file__).parent / 'public'
DATA_DIR = PUBLIC_DIR / 'data'

# Enable CORS for development
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


# ============================================================================
# API Endpoints
# ============================================================================

@app.route('/')
def home():
    """Main website"""
    return send_from_directory(PUBLIC_DIR, 'index.html')


@app.route('/data/daily-image.json')
def get_daily_image():
    """Serve today's image data"""
    try:
        with open(DATA_DIR / 'daily-image.json', 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify({'error': 'No data available'}), 404


@app.route('/data/archive.json')
def get_archive():
    """Serve archive of past images"""
    try:
        with open(DATA_DIR / 'archive.json', 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        # Return mock archive if file doesn't exist
        return jsonify([])


@app.route('/images/<filename>')
def serve_image(filename):
    """Serve image files"""
    return send_from_directory(PUBLIC_DIR / 'images', filename)


@app.route('/<path:path>')
def serve_static(path):
    """Serve other static files"""
    file_path = PUBLIC_DIR / path
    if file_path.is_file():
        return send_from_directory(PUBLIC_DIR, path)
    return jsonify({'error': 'Not found'}), 404


# ============================================================================
# Debug & Test Endpoints
# ============================================================================

@app.route('/api/status')
def status():
    """Check server status and available data"""
    has_daily = (DATA_DIR / 'daily-image.json').exists()
    has_archive = (DATA_DIR / 'archive.json').exists()
    
    return jsonify({
        'status': 'running',
        'timestamp': __import__('datetime').datetime.now().isoformat(),
        'data_available': {
            'daily_image': has_daily,
            'archive': has_archive
        }
    })


@app.route('/api/mock/flickr')
def mock_flickr():
    """Mock Flickr API response for testing"""
    return jsonify({
        'photos': {
            'photo': [
                {
                    'id': '12345678',
                    'title': 'Mock Historical Image',
                    'description': {'_content': 'A sample description'},
                    'url_o': 'https://via.placeholder.com/800x600?text=Mock+Image',
                    'datetaken': '1850-01-01 12:00:00',
                    'tags': 'mock test historical'
                }
            ]
        }
    })


@app.route('/api/mock/llava')
def mock_llava():
    """Mock LLaVA AI analysis for testing"""
    return jsonify({
        'generated_text': 'This is a mock AI analysis of a historical image. It describes the visual elements, historical context, artistic qualities, cultural significance, and atmospheric mood of the photograph in a scholarly Victorian manner.'
    })


# ============================================================================
# Development Utilities
# ============================================================================

@app.route('/dev')
def dev_dashboard():
    """Development dashboard"""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dev Dashboard - Daily Antiquarian</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f5f5f5; }
            h1 { color: #d5b034; }
            .section { background: white; padding: 20px; margin: 20px 0; border-left: 4px solid #d5b034; }
            .endpoint { background: #f0f0f0; padding: 10px; margin: 10px 0; font-family: monospace; }
            a { color: #d5b034; text-decoration: none; }
            a:hover { text-decoration: underline; }
            button { background: #d5b034; color: white; border: none; padding: 10px 20px; cursor: pointer; margin: 5px; }
            button:hover { background: #c5a024; }
        </style>
    </head>
    <body>
        <h1>⚙️ Development Dashboard</h1>
        
        <div class="section">
            <h2>🌐 Main Links</h2>
            <p><a href="/">← Main Website</a></p>
        </div>
        
        <div class="section">
            <h2>📊 API Endpoints</h2>
            
            <h3>Data API:</h3>
            <div class="endpoint">GET /data/daily-image.json</div>
            <p><button onclick="fetch('/data/daily-image.json').then(r=>r.json()).then(d=>console.log(d))">Test</button></p>
            
            <div class="endpoint">GET /data/archive.json</div>
            <p><button onclick="fetch('/data/archive.json').then(r=>r.json()).then(d=>console.log(d))">Test</button></p>
            
            <h3>Mock APIs (for testing):</h3>
            <div class="endpoint">GET /api/mock/flickr</div>
            <p><button onclick="fetch('/api/mock/flickr').then(r=>r.json()).then(d=>alert(JSON.stringify(d,null,2)))">Test</button></p>
            
            <div class="endpoint">GET /api/mock/llava</div>
            <p><button onclick="fetch('/api/mock/llava').then(r=>r.json()).then(d=>alert(JSON.stringify(d,null,2)))">Test</button></p>
        </div>
        
        <div class="section">
            <h2>🔍 Status</h2>
            <p><button onclick="fetch('/api/status').then(r=>r.json()).then(d=>alert(JSON.stringify(d,null,2)))">Check Status</button></p>
        </div>
        
        <div class="section">
            <h2>📁 File Structure</h2>
            <pre>
public/
├── index.html              (Main website)
├── data/
│   ├── daily-image.json    (Today's data)
│   └── archive.json        (Last 30 days)
├── images/
│   └── daily-*.jpg         (Downloaded images)
└── ...
            </pre>
        </div>
        
        <div class="section">
            <h2>💡 Quick Tips</h2>
            <ul>
                <li>Open DevTools (F12) to see Console logs</li>
                <li>Check Network tab to see API calls</li>
                <li>Edit daily-image.json to test UI updates</li>
                <li>Mock data is in public/data/daily-image.json</li>
            </ul>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500


# ============================================================================
# Server Startup
# ============================================================================

if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════════╗
║          🏛️  The Daily Antiquarian - Dev Server              ║
╚════════════════════════════════════════════════════════════════╝

📍 Main Website:  http://localhost:5000/
📊 Dev Dashboard: http://localhost:5000/dev
📋 API Status:    http://localhost:5000/api/status

📁 Serving from: {public_dir}

Press CTRL+C to stop the server.
    """.format(public_dir=PUBLIC_DIR))
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=True
    )

