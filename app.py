# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template, url_for
from inference_engine import diagnose_input
import json
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Archivo para guardar la retroalimentación
FEEDBACK_FILE = 'feedback.json'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    user_input = data.get('input', '')
    result = diagnose_input(user_input)
    return jsonify(result)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    feedback_data = {
        'timestamp': datetime.now().isoformat(),
        'diagnosis': data.get('diagnosis'),
        'was_helpful': data.get('wasHelpful')
    }
    
    try:
        # Cargar feedback existente
        try:
            with open(FEEDBACK_FILE, 'r') as f:
                feedback_history = json.load(f)
        except FileNotFoundError:
            feedback_history = []
        
        # Agregar nuevo feedback
        feedback_history.append(feedback_data)
        
        # Guardar feedback actualizado
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump(feedback_history, f, indent=2)
        
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)