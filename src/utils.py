# this have the common functionality the entire program use
import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok = True)

        with open(file_path, "wb")  as file_obj:
            dill.dump(obj,file_obj) 
    except Exception as e:
        raise CustomException(e,sys) from e
    
        
def evaluate_models(x_train, y_train, x_test ,y_test , models):
    try:
        report = {}
        for model_name, model in models.items():
            logging.info(f"Training model: {model_name}")
            model.fit(x_train, y_train)

            
            y_test_pred = model.predict(x_test)

            
            test_model_score = r2_score(y_test,y_test_pred)

            report[model_name] = test_model_score
            logging.info(f"{model_name} - Test R2 score: {test_model_score:.4f}")

        return report

    except Exception as e:
        raise CustomException(e, sys) from  e        
