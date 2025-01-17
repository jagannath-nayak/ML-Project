import os
import sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from xgboost import XGBRegressor
from sklearn.base import BaseEstimator, RegressorMixin

class SklearnCompatibleXGBRegressor(XGBRegressor, BaseEstimator, RegressorMixin):
    @staticmethod
    def __sklearn_tags__():
        return {}

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)        
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            try:
                print(f"Evaluating model: {model_name}")
                para = param.get(model_name, {})
                print(f"Parameters: {para}")

                # Initialize GridSearchCV
                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)

                # Set the best parameters and retrain
                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)

                # Predictions
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # Scoring
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)

                report[model_name] = test_model_score

            except Exception as inner_e:
                print(f"Error with model {model_name}: {inner_e}")

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)