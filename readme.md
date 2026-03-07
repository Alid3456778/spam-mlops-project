1. DVC Automation  :
so as the process are to clean the raw data and then save it into the processd folder 
that is done into the data folder , to do so we have to run the "python preprocess.py python train_model.py"
so we will now run this "dvc repro"

    dvc install 
    dvc init 
    dvc stage (An complex way to ymal the commands) 
        :->
            python -m dvc stage add -n preprocess \
            -d src/data/preprocess.py \
            -d data/raw/spam.csv \
            -o data/processed/clean_spam.csv \
            python src/data/preprocess.py
    dvc repro

SO now we have also stage the Model trainging thing , like simple we use to train model and the data would be saved into the models folder it will be done by the dvc 
            python -m dvc stage add -n train \
            -d src/training/train_model.py \
            -d data/processed/clean_spam.csv \
            -o models/spam_model.pkl \
            python src/training/train_model.py

2. MLFlow :
it does to add experement tracking and whenever you run the training model or code it save that this time the accuracy is this much and this much 
(You can see that in traning folder file i have added this)

            | Run   | Model      | Accuracy |
            | ----- | ---------- | -------- |
            | Run 1 | NaiveBayes | 0.75     |
            | Run 2 | NaiveBayes | 0.78     |

You are now saving and Tracking the Model Accuracy with the help of the MLFlow 

3.FastAPI :
As to show this code into the real world we have to deploy in into somewhere in the world and this we can do with the help of the API (Application Programming Interface) It is a way to find thing in the internet by there name , the name can be the IP:PORT and more 
So we use the fastapi to make it into the api and use uvicorn to host them

    python -m uvicorn api.app:app --reload

this will start the api and host it into the local at 8000 
    http://127.0.0.1:8000/docs 
        |
        |> this is to access the website api , and there is the POST  option this will use to get the message will use to run
    
So from running the file from the python to accessing the code from the website localhost