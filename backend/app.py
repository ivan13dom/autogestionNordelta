from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Esto permite que tu GitHub Pages se conecte

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Servidor Andreani Nordelta (Python) Activo", "sucursal": "Nordelta"})

if __name__ == '__main__':
    # Usamos el puerto que nos asigne Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)