from flask import Flask, request, jsonify
from main import run

app = Flask(__name__)

@app.post('/api/ai')
def image():
    pill_color, pill_shape, pill_text = run()
    return jsonify({
        "pill_color": pill_color,
        "pill_shape": pill_shape,
        "pill_text": pill_text
    })

if __name__=="__main__":
    app.run('0.0.0.0', port=5000, debug=True)