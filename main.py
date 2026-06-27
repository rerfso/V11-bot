from fastapi import FastAPI

app = FastAPI()

@app.post("/chat")
def chat(data: dict):

    text = data["text"]

    return {
        "response": f"📖 Ты написал: {text}\n\n🧠 API работает"
    }
