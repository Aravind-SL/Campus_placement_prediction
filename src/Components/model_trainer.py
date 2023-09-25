import os
import sys
from dataclasses import dataclass

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str= os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Entered model trainer. Splitting train and test dataset.')

            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                        "Logistic Regression": LogisticRegression(),
                        "K-Neighbors Classifier": KNeighborsClassifier(),
                        "Decision Tree Classifier": DecisionTreeClassifier(),
                        "Random Forest Classifier": RandomForestClassifier(),
                        "SVM Classifier": SVC(),
                        "XGBoost Classifier": XGBClassifier(),
                        "CatBoost Classifier": CatBoostClassifier(verbose=False),
                        "AdaBoost Classifier": AdaBoostClassifier()
                    }
            model_report= evaluate_model(X_train=x_train, y_train= y_train, X_test= x_test, y_test= y_test, models= models) 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]
            logging.info('Best model found.')

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(x_test)
            acc_value = accuracy_score(y_test, predicted)
            return f"Model name: {best_model_name}\nr2_score: {acc_value}"
        
        except Exception as e:
            raise CustomException(e, sys)