from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import json

# Example config dictionary to map intents to numbers
intent_config = {
    "regular_conversation": 1,   # For mental health conversations and exercises
    "product_related": 2,        # For inquiries about how Clare works and communication methods
    "subscription_related": 3,   # For questions about user subscriptions and trial periods
    "suicide": 4,                # For detecting and addressing indications of suicidal thoughts
    "non_mental_health": 5,      # For steering conversations back to mental health topics
    "greet": 6,
    "goodbye": 7,
    "deny": 8,
    "affirm": 9,
    "bot_challenge": 10
}


app = FastAPI()


class InputText(BaseModel):
    text: str


@app.post("/parse/")
async def parse_text(input: InputText):
    url = "http://localhost:5005/model/parse"
    try:
        # Asynchronously send the request to the model
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"text": input.text})
        data = response.json()

        # Extract the most likely intent and its confidence
        intent_name = data['intent']['name']
        confidence = data['intent']['confidence']

        # Get the intent number from the config
        intent_number = intent_config.get(intent_name, -1)  # Return -1 if intent is not found in config

        return {
            "intent": intent_name,
            "confidence": confidence,
            "intent_number": intent_number
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
