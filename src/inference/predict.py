import pickle


def load_model():
    with open("models/spam_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)
    return model, vectorizer


def predict_message(message):

    model, vectorizer = load_model()

    # convert message to vector
    message_vector = vectorizer.transform([message])

    # predict
    prediction = model.predict(message_vector)

    return prediction[0]


def main():

    message = input("Enter a message: ")

    result = predict_message(message)

    print("Prediction:", result)


if __name__ == "__main__":
    main()