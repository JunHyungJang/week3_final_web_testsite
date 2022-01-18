# import sys
import numpy as np
# import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Activation
from keras import metrics
from tensorflow.keras.optimizers import SGD
import easydict
import numpy as np
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torch.utils.data import Dataset,DataLoader
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model


model = load_model('Analysis_20_final_5.h5')
print(model.layers[2].get_weights())
x_test = 0
y_test = 0
x_test= np.array([[22,13,25,124,102,111,83,101,111,73,51,50,52,50,50,35,54,50,50,50]])
x_test_1= np.array([[1,1,1,1,1,44,71,81,91,101,18,91,51,61,21,51,51,51,51,51]])

print(np.shape(x_test_1))
y_predict_1 = model.predict(x_test_1)
print(y_predict_1)
print("당신이 승리할 확률은 {0}% 입니다".format(y_predict_1[0][0] * 100))
