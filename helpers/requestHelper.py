import os
import requests
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv('OPENAI_API_KEY')


def aiChat(chatMessage):
    url = "https://api.openai.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"{chatMessage}"
            }
        ],
        "temperature": 0.7
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{secret}"
    }

    response = requests.request("POST", url, json=payload, headers=headers).json()
    choices = response["choices"]
    messageList = choices[0]
    message = messageList["message"]

    return message['content']
