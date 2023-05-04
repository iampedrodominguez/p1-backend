from fastapi import FastAPI
import openai
from dotenv import load_dotenv

import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(request: dict):
    text = request["message"]

    prompt = {"role": "system", "content": "You are a helpful assistant."}
    user = {"role": "user", "content": "You suck ass"}

    print("TEST")

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature=0.7,
        messages = [prompt, user]
        )

    print(f"{response.choices[0].message.content}")
    # return {"message": response.choices[0].text.strip()}
