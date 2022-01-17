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

model = load_model('Analysis.h5')

x_test= np.array([[112,31,90,132,102,142,83,101,111,73]])
y_predict = model.predict(x_test)
print(y_predict)
print("당신이 승리할 확률은 {0}% 입니다".format(y_predict[0][1] * 100))

