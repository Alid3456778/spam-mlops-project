import pandas as pd
import pickle
import mlflow

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():

    # Load cleaned dataset
    data = pd.read_csv("data/processed/clean_spam.csv")

    X = data["message"]
    y = data["label"]

    # Convert text into numbers
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    # Split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, y, test_size=0.2, random_state=42
    )
    with mlflow.start_run():
        model = MultinomialNB()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("Model Accuracy:", accuracy)

        mlflow.log_param("model_type", "MultinomialNB")
        mlflow.log_metric("accuracy", accuracy)

    # Train model
    # model = MultinomialNB()
    # model.fit(X_train, y_train)

    # Predict on test data
    predictions = model.predict(X_test)

    # Calculate accuracy
    # accuracy = accuracy_score(y_test, predictions)

    # print("Model Accuracy:", accuracy)
    accuracy = accuracy_score(y_test, predictions)

    print("Model Accuracy:", accuracy)

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    
    # Save model
    with open("models/spam_model.pkl", "wb") as f:
        pickle.dump((model, vectorizer), f)

    print("Model saved to models/spam_model.pkl")


if __name__ == "__main__":
    main()