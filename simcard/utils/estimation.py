import tensorflow as tf
import numpy as np
from customer_segmentation.settings import BASE_DIR
from tensorflow.keras.metrics import MeanSquaredError


PATH =  BASE_DIR.as_posix() + "/data/models/"


class SimValueEstimation:

    def __init__(self) -> None:
        self._912model = tf.keras.models.load_model(PATH+'ranking_model_with_912.h5', custom_objects={'mse': MeanSquaredError}) 
        self._no912model = tf.keras.models.load_model(PATH+'ranking_model_without_912.h5', custom_objects={'mse': MeanSquaredError})

    def get_features(self, phonenumber):
        """
        return dict features
        """
        one_hot_sequence = [np.eye(10)[int(digit)] for digit in phonenumber[1:]]
        return one_hot_sequence

    def get_predict(self, phonenumber):
        if phonenumber[1:4] == "912":
            model =  self._912model
        else:
            model = self._no912model

        one_hot_sequence = self.get_features(phonenumber)
        predicted_log_price = model.predict(np.array([one_hot_sequence]), verbose=0)[0][0]
        
        return (2 ** predicted_log_price) - 1
    