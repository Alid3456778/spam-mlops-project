import os
import pickle
import threading
import time
import requests
from fastapi import FastAPI

# Optional dotenv (safe)
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass
app = FastAPI()


# Load model
def load_model():
    with open("models/spam_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)
    return model, vectorizer


model, vectorizer = load_model()


@app.get("/")
def home():
    return {"message": "Spam Detection API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(message: str):

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)

    return {"prediction": prediction[0]}

# ---------------- KEEP ALIVE ----------------
def start_keep_alive():
    url = os.getenv("RENDER_EXTERNAL_URL")

    if not url:
        print("[KeepAlive] No URL found")
        return

    full_url = url + "/health"

    def ping():
        while True:
            try:
                res = requests.get(full_url)
                print(f"[KeepAlive] Ping: {res.status_code}")
            except Exception as e:
                print("[KeepAlive Error]", e)

            time.sleep(600)  # 10 minutes

    thread = threading.Thread(target=ping, daemon=True)
    thread.start()


# Start keep alive when app starts
start_keep_alive()