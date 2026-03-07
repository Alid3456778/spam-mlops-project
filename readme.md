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


4.Docker :
As the comapny employee says , "IT WORKS ON MY COMPUTER" its a thing that is very funny and idotic at the same time how can you say that it works on my machine and not yours  .
to solve this the Docker and Docker Conatiners come in image (Did you see how i put image inside the sentence 😁 ).
so we create an Docker file which will contanarise ower application in simple step of installation , what it does is get all your thing (commands) to start the application and put it into the file like :
    1.which Directory
    2.which Files
    3.Where in the Docker
    4.What Depemdencys
    5.How to start the Application

and when the image is formed we just simple run (Build) it and set the PORT and acees it 

5.GitAction:
It is a way of automatic building and testing thing and every thing from building to using the application it comes under this file with each command.
So in this the full working application comes and have everything in it from dependencys to docker build command .
Some users add the test file so before production hit we can check wether the code is working or crash out .
Its a practice that we should do avoid the error , its like the Last safe check test which do everything that we need to do and deploy it .
It run automatically when we just push it to the intented Branch which i have is "main" we can also set it onto pull condition also .

