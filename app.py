from fastapi import FastAPI
import openai
import os

app = FastAPI()
openai.api_key = "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"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(request: dict):
    text = request["message"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Sentiment analysis of the following text:\n{text}\n",
        temperature=0.5,
        max_tokens=100, 
        top_p=1, 
        frequency_penalty=0,
        presence_penalty=0 
    )
    return {"message": response.choices[0].text.strip()}
