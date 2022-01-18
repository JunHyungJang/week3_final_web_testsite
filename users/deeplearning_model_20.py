import sys
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Activation
from keras import metrics
from tensorflow.keras.optimizers import SGD
import easydict

import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
import urllib

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)


lolChampion = {
    '가렌': 1, '갈리오': 2, '갱플랭크': 3, '그라가스': 4, '그레이브즈': 5, '그웬': 6, '나르': 7, '나미': 8, '나서스': 9, '노틸러스': 10, 
    '녹턴': 11, '누누와 윌럼프': 12, '니달리': 13, '니코': 14, '다리우스': 15, '다이애나': 16, '드레이븐': 17, '라이즈': 18, '라칸': 19, '람머스': 20,
    '럭스': 21, '럼블': 22, '레넥톤': 23, '레오나': 24, '렉사이': 25, '렐': 26, '렝가': 27, '루시안': 28, '룰루': 29, '르블랑': 30,
    '리 신': 31, '리븐': 32, '리산드라': 33, '릴리아': 34, '마스터 이': 35, '마오카이': 36, '말자하': 37, '말파이트': 38, '모데카이저': 39, '모르가나': 40,
    '문도 박사': 41, '미스 포츈': 42, '바드': 43, '바루스': 44, '바이': 45, '베이가': 46, '베인': 47, '벡스': 48, '벨코즈': 49, '볼리베어': 50,
    '브라움': 51, '브랜드': 52, '블라디미르': 53, '블리츠크랭크': 54, '비에고': 55, '빅토르': 56, '뽀삐': 57, '사미라': 58, '사이온': 59, '사일러스': 60,
    '샤코': 61, '세나': 62, '세라핀': 63, '세주아니': 64, '세트': 65, '소나': 66, '소라카': 67, '쉔': 68, '쉬바나': 69, '스웨인': 70,
    '스카너': 71, '시비르': 72, '신 짜오': 73, '신드라': 74, '신지드': 75, '쓰레쉬': 76, '아리': 77, '아무무': 78, '아우렐리온 솔': 79, '아이번': 80,
    '아지르': 81, '아칼리': 82, '아크샨': 83, '아트록스': 84, '아펠리오스': 85, '알리스타': 86, '애니': 87, '애니비아': 88, '애쉬': 89, '야스오': 90,
    '에코': 91, '엘리스': 92, '오공': 93, '오른': 94, '오리아나': 95, '올라프': 96, '요네': 97, '요릭': 98, '우디르': 99, '우르곳': 100,
    '워윅': 101, '유미': 102, '이렐리아': 103, '이블린': 104, '이즈리얼': 105, '일라오이': 106, '자르반 4세': 107, '자야': 108, '자이라': 109, '자크': 110,
    '잔나': 111, '잭스': 112, '제드': 113, '제라스': 114, '제이스': 115, '조이': 116, '직스': 117, '진': 118, '질리언': 119, '징크스': 120,
    '초가스': 121, '카르마': 122, '카밀': 123, '카사딘': 124, '카서스': 125, '카시오페아': 126, '카이사': 127, '카직스': 128, '카타리나': 129, '칼리스타': 130,
    '케넨': 131, '케이틀린': 132, '케인': 133, '케일': 134, '코그모': 135, '코르키': 136, '퀸': 137, '클레드': 138, '키아나': 139, '킨드레드': 140,
    '타릭': 141, '탈론': 142, '탈리야': 143, '탐 켄치': 144, '트런들': 145, '트리스타나': 146, '트린다미어': 147, '트위스티드 페이트': 148, '트위치': 149, '티모': 150,
    '파이크': 151, '판테온': 152, '피들스틱': 153, '피오라': 154, '피즈': 155, '하이머딩거': 156, '헤카림': 157
    }


users = list()
for i in range(200,250): #한 페이지당 100명 유저 -> 1페이지부터 시작함.
  userUrl = 'https://www.op.gg/ranking/ladder/page=' + str(i)
  userRes = req.get(userUrl, headers=hdr)
  if userRes.status_code != 200:
    print(userUrl,"페이지에서 에러가 발생했습니다.")
    print(userRes.status_code)
    break
  userHtml = userRes.text
  userSoup = BeautifulSoup(userHtml, 'html.parser')

  getUser = userSoup.select("tr.ranking-table__row > td.ranking-table__cell.ranking-table__cell--summoner > a > span")
  for userName in getUser:
    users.append(userName.text.strip())
print(users)


number = [
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
          '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
          '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
          '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'
          ]


def winRate(userID):
  winName = urllib.parse.quote(userID)
  winUrl = "https://www.op.gg/summoner/userName=" + winName + "?l=ko_KR"
  winRes = req.get(winUrl, headers=hdr)
  if userRes.status_code != 200:
    print(winUrl,"페이지에서 에러가 발생했습니다.")
    print(winRes.status_code)
    rate = 0
    return rate
  winHtml = winRes.text
  winSoup = BeautifulSoup(winHtml, 'html.parser')
  description = winSoup.find("meta", attrs={"name":"description"})
  descript = description["content"]
  descriptRate = list()
  winDescript = ""
  count = 0
  for k in range(len(descript)):
    if count == 2:
      descriptRate.append(descript[k])
    if descript[k] == "/":
      count += 1
  winnerRate = descriptRate[len(descriptRate)-6:len(descriptRate)-3]
  winner = ""
  for h in range(len(winnerRate)):
    if winnerRate[h].isdigit() == True:
      winner += winnerRate[h]
  if winner in number:
    win = int(winner)
  else:
    win = 0
  return win


xData = list()
yData = list()


playChampion = list()
otherPlayerRate = list()
check = 0
info = False

for i in range(0, 500):
  urlName = urllib.parse.quote(users[i])
  print("랭킹",i+1,"위:",urlName)
  championUrl = "https://www.op.gg/summoner/userName=" + urlName + "?l=ko_KR"
  driver.get(championUrl)
  championHtml = driver.page_source
  championSoup = BeautifulSoup(championHtml, "html.parser")
  championTeam = championSoup.find_all("div", attrs={"class": "Team"})
  championResult = championSoup.find_all("div", attrs={"class": "GameResult"})
  gameType = championSoup.find_all("div", attrs={"class": "GameType"})
  otherName = championSoup.find_all("div", attrs={"class": "SummonerName"})
  player = 0
  

  for j in range(0, len(championResult)*2, 2):
    result = championResult[j//2].text.strip()
    teamOne = championTeam[j].find_all("div")
    game = gameType[j//2].text.strip()

    for p in range(2, len(teamOne), 5):
      if teamOne[p-2]["class"][1] == "Requester":
        if result == "승리":
          resultChampion = [1,0]
          info = True
        elif result == "패배":
          resultChampion = [0,1]
          info = True
        else:
          resultChampion = "None"
      playChampion.append(lolChampion[teamOne[p].text.strip()])
      check += 5
      otherPlayerRate.append(winRate(otherName[player].text.strip()))
      player += 1
    check = 0
    
    teamTwo = championTeam[j+1].find_all("div")
    for q in range(2, len(teamTwo), 5):
      if teamTwo[q-2]["class"][1] == "Requester":
        if result == "승리":
          resultChampion = [0,1]
          info = True
        elif result == "패배":
          resultChampion = [1,0]
          info = True
        else:
          resultChampion = "None"
      playChampion.append(lolChampion[teamTwo[q].text.strip()])
      check += 5
      otherPlayerRate.append(winRate(otherName[player].text.strip()))
      player += 1
    check = 0

    if info == True and game == "솔랭":
      xData.append(playChampion + otherPlayerRate)
      yData.append(resultChampion)
    info = False
    playChampion = list()
    otherPlayerRate = list()

print("Crawling Complete")


print("Show Dataset")
print(xData)
print(yData)
print("Users Data:",len(users))
print("Champions Data:",len(xData))
print("Results Data:",len(yData))


countDel = 0
for w in range(len(xData)):
  if len(xData[w]) != 20:
    print("X Data의",w,"번째 데이터가 이상합니다.")
    countDel += 1
  if len(yData[w]) != 2:
    print("Y Data의",w,"번째 데이터가 이상합니다.")
    countDel += 1
if countDel > 0:
  print("데이터에 수정이 필요합니다.")


x = np.array(xData)
print(np.shape(x))
y = np.array(yData)
print(np.shape(y))

model = Sequential()
model.add(Dense(32, activation = 'relu', input_shape= (20,)))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(2, activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.summary()

hist = model.fit(x,y,epochs = 20)
results = model.evaluate(x,y)
print(results)


x_tests = np.array([[112,31,1,12,102,142,83,101,111,1,1,1,1,1,1,49,53,60,49,56]])

y_predicts = model.predict(x_tests)

print(y_predicts)

print("당신이 승리할 확률은 {0}% 입니다".format(y_predicts[0][0] * 100))


model.save("Analysis_20.h5")








