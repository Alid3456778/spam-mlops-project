import pandas as pd
import re


# Function to clean text
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()  # convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation and numbers
    text = text.strip()  # remove extra spaces
    return text


def main():

    # Load raw dataset
    data = pd.read_csv("data/raw/spam.csv")

    # Ensure there are no missing messages
    data["message"] = data["message"].fillna("")

    # Clean the message column
    data["message"] = data["message"].apply(clean_text)

    # Save processed dataset
    data.to_csv("data/processed/clean_spam.csv", index=False)

    print("Data preprocessing completed")
    print("Clean dataset saved to data/processed/clean_spam.csv")


if __name__ == "__main__":
    main()