from fastapi import FastAPI
import pickle

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


@app.post("/predict")
@app.get("/predict")
def predict(message: str):

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)

    return {"prediction": prediction[0]}