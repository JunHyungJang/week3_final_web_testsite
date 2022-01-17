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

champion_name = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu',
             'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelionsol', 'Azir',
             'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille',
             'Cassiopeia', 'Chogath', 'Corki', 'Darius', 'Diana', 'Drmundo',
             'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks',
             'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
             'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi',
             'Irelia', 'Ivern', 'Janna', 'Jarvaniv', 'Jax', 'Jayce',
             'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Karma', 'Karthus',
             'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Khazix',
             'Kindred', 'Kled', 'Kogmaw', 'Leblanc', 'Leesin', 'Leona',
             'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite',
             'Malzahar', 'Maokai', 'Masteryi', 'Missfortune', 'Mordekaiser', 'Morgana',
             'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne',
             'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy',
             'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', 'Reksai',
             'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze',
             'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco',
             'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner',
             'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahmkench',
             'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana',
             'Trundle', 'Tryndamere', 'Twistedfate', 'Twitch', 'Udyr', 'Urgot',
             'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vex', 'Vi',
             'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Monkeyking',
             'Xayah', 'Xerath', 'Xinzhao', 'Yasuo', 'Yone', 'Yorick',
             'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

model = load_model('Analysis.h5')

def calculate(datalist):
    model = load_model('Analysis.h5')
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