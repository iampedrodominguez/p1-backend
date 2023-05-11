from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware


# Import Azure libraries
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8000/chat",
    "https://analysis-result.azurewebsites.net/chat",
    "https://act-is-2-elim-plant.vercel.app/"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(request: dict):
    app = request["app"]
    text = request["message"]

    logging.info('REVIEW RECEIVED')

    prompt = {"role": "system", "content": "You are an assistant in Google Play's customer service team. Your job is to receive feedback and reviews from the user. In the case of mixed reviews, be thankful for the good parts and helpful with the bad parts. "}
    user = {"role": "user", "content": f"App: {app}. Review: {text}"}
    
    logging.info('AI THINKING')


    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature=0.7,
        messages = [prompt, user]
        )

    logging.info('RESPONSE SENT')
    return response.choices[0].message.content
