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

champion_name = [
    'Garen', 'Galio', 'Gangplank', 'Gragas', 'Graves', 'Gwen',
    'Gnar', 'Nami', 'Nasus', 'Nautilus', 'Nocturne', 'Nunu',
    'Nidalee', 'Neeko', 'Darius', 'Diana', 'Draven', 'Ryze',
    'Rakan', 'Rammus', 'Lux', 'Rumble', 'Renekton', 'Leona',
    'Reksai', 'Rell', 'Rengar', 'Lucian', 'Lulu', 'Leblanc',
    'Leesin', 'Riven', 'Lissandra', 'Lillia', 'Masteryi', 'Maokai',
    'Malzahar', 'Malphite', 'Mordekaiser', 'Morgana', 'Drmundo', 'Missfortune',
    'Bard', 'Varus', 'Vi', 'Veigar', 'Vayne', 'Vex',
    'Velkoz', 'Volibear', 'Braum', 'Brand', 'Vladimir', 'Blitzcrank',
    'Viego', 'Viktor', 'Poppy', 'Samira', 'Sion', 'Sylas',
    'Shaco', 'Senna', 'Seraphine', 'Sejuani', 'Sett', 'Sona',
    'Soraka', 'Shen', 'Shyvana', 'Swain', 'Skarner', 'Sivir',
    'Xinzhao', 'Syndra', 'Singed', 'Thresh', 'Ahri', 'Amumu',
    'Aurelionsol', 'Ivern', 'Azir', 'Akali', 'Akshan', 'Aatrox',
    'Aphelios', 'Alistar', 'Annie', 'Anivia', 'Ashe', 'Yasuo',
    'Ekko', 'Elise', 'Monkeyking', 'Ornn', 'Orianna', 'Olaf',
    'Yone', 'Yorick', 'Udyr', 'Urgot', 'Warwick', 'Yuumi',
    'Irelia', 'Evelynn', 'Ezreal', 'Illaoi', 'Jarvaniv', 'Xayah',
    'Zyra', 'Zac', 'Janna', 'Jax', 'Zed', 'Xerath',
    'Jayce', 'Zoe', 'Ziggs', 'Jhin', 'Zilean', 'Jinx',
    'Chogath', 'Karma', 'Camille', 'Kassadin', 'Karthus', 'Cassiopeia',
    'Kaisa', 'Khazix', 'Katarina', 'Kalista', 'Kennen', 'Caitlyn',
    'Kayn', 'Kayle', 'Kogmaw', 'Corki', 'Quinn', 'Kled',
    'Qiyana', 'Kindred', 'Taric', 'Talon', 'Taliyah', 'Tahmkench',
    'Trundle', 'Tristana', 'Tryndamere', 'Twistedfate', 'Twitch', 'Teemo',
    'Pyke', 'Pantheon', 'Fiddlesticks', 'Fiora', 'Fizz', 'Heimerdinger', 'Hecarim'
]

model = load_model('Analysis_10_final_5.h5')

def calculate(datalist):
    x_test = 0
    y_predict = 0
    # model = load_model('Analysis_10_final_2.h5')
    print("reach here2")
    print(datalist)
    print(champToIndex(datalist))
    # x_test= np.array([[112,31,90,132,102,142,83,101,111,73]])
    x_test = np.array([champToIndex(datalist)])
    print(np.shape(x_test))
    y_predict = model.predict(x_test)
    print(y_predict)
    print("당신이 승리할 확률은 {0}% 입니다".format(y_predict[0][0] * 100))

    return y_predict[0][0] * 100

def champToIndex(datalist): 
    temp = []
    for i in range(len(datalist)):
        print(datalist[i])
        temp.append(champion_name.index(datalist[i])+1)
    return temp