# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import controller as co
import concurrent.futures
import os
import sys

app = Flask(__name__)

def process_text(text):
    """Función auxiliar para procesar un solo texto con la clasificación de spam."""
    return co.classi_spam(text)

@app.route('/', methods=['POST'])
def classify_texts():
    content = request.get_json()

    # Verificamos si la clave "texts" está presente
    if not content or 'texts' not in content:
        return jsonify({"error": "Falta la clave 'texts' en el JSON"}), 400

    texts = content['texts']

    # Verificamos que sea una lista de textos
    if not isinstance(texts, list):
        return jsonify({"error": "'texts' debe ser una lista"}), 400

    num_workers = min(len(texts), 8)  # 🔹 Limitar a 8 workers en lugar de usar `os.cpu_count()`

    # 🔥 PROCESAMIENTO CON MULTIHILOS (más rápido que procesos)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_text, texts))

    return jsonify(results), 200

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
