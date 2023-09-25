import os
import pickle
import sys

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report={}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            logging.info(f"In the model: {model}")
            
            model.fit(X_train, y_train)
            
            y_test_pred = model.predict(X_test)
            test_model_score = accuracy_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
            logging.info(f'Completed: {model}')
        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_model(file_path):
    try:
        with open(file_path, 'rb') as obj:
            return pickle.load(obj)

    except Exception as e:
        raise CustomException(e, sys)