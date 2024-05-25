from flask import Flask, request, jsonify
import openai
from chatbot import predict

app = Flask(__name__)

@app.post('/api/ai')
def chat():
    data = request.get_json()
    message = data['message']
    history_list = data['history']

    # # history_list를 필요한 형식으로 변환 (str 리스트를 dict 리스트로 변환)
    # formatted_history = [{"role": "user" if i % 2 == 0 else "assistant", "content": h} for i, h in
    #                      enumerate(history_list)]

    history_list.append(message)

    # predict 함수 호출
    response = predict(history_list)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
