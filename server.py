from flask import Flask, request, jsonify
from main import run
import opanai
from chatbot import predict

app = Flask(__name__)

@app.post('/api/ai')
def image():
    pill_color, pill_shape, pill_text = run()
    return jsonify({
        "pill_color": pill_color,
        "pill_shape": pill_shape,
        "pill_text": pill_text
    })

@app.post('/api/ai')
def chat():
    data = request.get_json()
    message = data['message']
    history_list = data['history']

    history_list.append(message)

    response = predict(history_list)
    
    return jsonify({'response': response})

if __name__=="__main__":
    app.run('0.0.0.0', port=5000, debug=True)