import openai
import random
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
print(openai_api_key)

random.seed(42)

def predict(input_history):

    history = [{ #시스템 메시지를 포함하는 창
        "role": "system",
        "content": "당신은 친절한 의약품 챗봇입니다. 입력에 대해 사용자가 이해하기 쉽게 친절하게 대답해주세요. 증상에 맞게 필요한 약을 추천해주고 사용자가 궁금한 점을 물어보면 사실 기반으로 대답을 제공해 주세요. "
    }]

    for i in range(len(input_history)):
        if (i + 1)%2==1:
            history.append({"role": "user", "content" : input_history[i]})
        else:
            history.append({"role": "assistant", "content": input_history[i]})

    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )

    response = gpt_response["choices"][0]["message"]["content"]
    
    return response
#print("당신은 친절한 의약품 챗봇입니다.")

def run():
    history = []
    while True:
        user_input = input("사용자: ")
        history.append(user_input)
        if(user_input == "종료"):
            break
        response = predict(history)
        history.append(response)
        print("챗봇:", response)


if __name__ == "__main__":
    run()
