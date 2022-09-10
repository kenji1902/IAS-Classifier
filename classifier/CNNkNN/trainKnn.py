import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import os.path
import joblib
if __name__ == '__main__':
    fileName = "IASleavesv4"
    Path = "static/classifier/classification_models"
    CNNModel = f'{fileName}.h5'
    CNNModelPath = f'{Path}/CNN/{CNNModel}'
    kNNModel = f'{fileName}.pkl'
    kNNModelPath = f'{Path}/kNN/{kNNModel}_{sklearn.__version__}'
    aug_x_trainArray = f'{fileName}.npy'
    aug_x_trainArrayPath = f'{Path}/aug_x_train/{aug_x_trainArray}'
    aug_y_trainArray = f'{fileName}.npy'
    aug_y_trainArrayPath = f'{Path}/aug_y_train/{aug_y_trainArray}'

    model = tf.keras.models.load_model(CNNModelPath)
    model_feat = keras.Model(inputs=model.input,outputs=model.get_layer('featureLayer').output)
    print('CNN loaded')

    aug_x_train = np.load(aug_x_trainArrayPath)
    print('aug_x_train loaded')

    aug_y_train = pd.read_csv(aug_y_trainArrayPath,index_col=0)
    aug_y_train = aug_y_train.squeeze()
    print('aug_y_train loaded')


    feat_train = model_feat.predict(aug_x_train)
    print('leaded features')

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(feat_train,aug_y_train)
    print("saved kNN")
    joblib.dump(knn, kNNModelPath)  