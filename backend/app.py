from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
import os, uuid, time
from PIL import Image

app = Flask(__name__)
CORS(app)

# 🟢 Endpoint raíz para probar que el backend funciona
@app.route('/')
def home():
    return "Backend OK"

# Carpeta uploads absoluta dentro del contenedor
UPLOAD_FOLDER = '/app/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
share_store = {}  # token -> {id, expires_at}

# Subir imagen
@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    f = request.files.get('image')
    if not f:
        return jsonify({'error': 'no file'}), 400
    img_id = str(uuid.uuid4())
    filename = f"{img_id}_{f.filename}"
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)
    return jsonify({'id': img_id, 'filename': filename, 'url': f'/uploads/{filename}'})

# Listar imágenes
@app.route('/api/list_images', methods=['GET'])
def list_images():
    files = os.listdir(UPLOAD_FOLDER)
    items = []
    for fn in files:
        parts = fn.split('_', 1)
        items.append({'id': parts[0], 'filename': fn, 'url': f'/uploads/{fn}'})
    return jsonify(items)

# Analizar imagen
@app.route('/api/analyse_image', methods=['POST'])
def analyse_image():
    data = request.json or {}
    img_id = data.get('id')
    if not img_id:
        return jsonify({'error': 'no id'}), 400
    for fn in os.listdir(UPLOAD_FOLDER):
        if fn.startswith(img_id + "_"):
            path = os.path.join(UPLOAD_FOLDER, fn)
            im = Image.open(path)
            return jsonify({
                'id': img_id,
                'filename': fn,
                'format': im.format,
                'size': im.size,
                'filesize_bytes': os.path.getsize(path)
            })
    return jsonify({'error': 'not found'}), 404

# Generar share link
@app.route('/api/share_image', methods=['POST'])
def share_image():
    data = request.json or {}
    img_id = data.get('id')
    if not img_id:
        return jsonify({'error': 'no id'}), 400
    token = str(uuid.uuid4())[:8]
    expires_at = int(time.time()) + 10*60  # 10 minutos
    share_store[token] = {'id': img_id, 'expires_at': expires_at}
    url = f"/s/{token}"
    return jsonify({'token': token, 'url': url, 'expires_at': expires_at})

# Página pública del share
@app.route('/s/<token>', methods=['GET'])
def shared_page(token):
    info = share_store.get(token)
    if not info or info['expires_at'] < int(time.time()):
        return "Link expired or not found", 404
    img_id = info['id']
    for fn in os.listdir(UPLOAD_FOLDER):
        if fn.startswith(img_id + "_"):
            img_url = f"/uploads/{fn}"
            html = f"""<!doctype html><html><head>
<meta property="og:title" content="Shared image"/>
<meta property="og:image" content="{img_url}"/>
</head><body><h1>Shared image</h1><img src="{img_url}" style="max-width:100%"></body></html>"""
            return render_template_string(html)
    return "Image not found", 404

# Servir imágenes subidas
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
