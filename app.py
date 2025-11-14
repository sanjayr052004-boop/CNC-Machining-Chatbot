from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
import re
from difflib import SequenceMatcher

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Load knowledge base
def load_knowledge_base():
    try:
        with open('knowledge_base.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"conversations": []}

knowledge_base = load_knowledge_base()

def find_similar_response(user_input):
    """Find the most similar response from knowledge base"""
    user_input_lower = user_input.lower()
    best_match = None
    highest_ratio = 0
    
    # Sample responses for demo
    responses = {
        "what is cnc": "CNC stands for Computer Numerical Control. It's a machine tool that uses computer control systems to automate the machining of parts.",
        "types of cnc machines": "Common CNC machines include CNC mills, CNC lathes, CNC routers, plasma cutters, and waterjet cutters.",
        "feed rate": "Feed rate is the speed at which the cutting tool moves through the material. It depends on material type, tool, and desired finish.",
        "spindle speed": "Spindle speed is measured in RPM. Higher speeds work for softer materials, lower speeds for harder materials.",
        "tool selection": "Tool selection depends on material type, required tolerances, surface finish, and cost. Carbide tools work well for most applications.",
        "g-code": "G-code is a programming language used to control CNC machines. G0 is rapid movement, G1 is linear movement.",
        "m-code": "M-code controls machine functions like spindle on/off, coolant on/off, and tool change.",
        "troubleshooting": "Common issues: tool chatter (reduce speed/feed), poor finish (check tool condition), broken tools (check for collisions)."
    }
    
    for key, response in responses.items():
        ratio = SequenceMatcher(None, user_input_lower, key).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = response
    
    if highest_ratio > 0.3:
        return best_match, highest_ratio
    else:
        return "I'm not sure about that. Could you provide more details about your CNC machining question?", 0.1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        response, confidence = find_similar_response(user_message)
        
        return jsonify({
            'response': response,
            'confidence': round(confidence * 100, 1),
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
