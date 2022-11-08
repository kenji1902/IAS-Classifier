import os.path
import joblib
# from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.python.keras import models, layers

from tensorflow import keras
from sklearn.neighbors import KNeighborsClassifier
import pprint

import os
import pandas as pd
import numpy as np
from classifier.CNNkNN import constants as c

resize_and_rescale = tf.keras.Sequential([
  tf.keras.layers.Resizing(256, 256),
  tf.keras.layers.Rescaling(1./255),
])

def loadData(load = ['CNN','kNN']):
    model_feat = None
    knn = None

    if 'CNN' in load:
        model = tf.keras.models.load_model(c.CNNModelPath)
        model_feat = keras.Model(inputs=model.input,outputs=model.get_layer('featureLayer').output)
        print('CNN loaded')

    if 'kNN' in load:
        knn = joblib.load(c.kNNModelPath)
        print('kNN loaded')

    return knn,model_feat

# ------- Load Trained Model --------
print("---Loading Model---")
knn, model_feat = loadData()
# ------- Load Trained Model --------

def predict( x_identify):
    feat_test = model_feat.predict(x_identify)

    # score = knn.score(feat_test,y_test)
    # print(score)
    predictionList = []

    prediction = knn.predict(feat_test)
    proba = knn.predict_proba(feat_test)
    for i,pred in enumerate(prediction):
        probability = max(proba[i])
        print(probability)
        if probability > 0.5:
            # print("The prediction for this image is: ", c.class_names[pred]," probability: ",probability)
            predictionList.append(c.class_names[pred])
        else:
            predictionList.append('no prediction')

    return predictionList