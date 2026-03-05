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

