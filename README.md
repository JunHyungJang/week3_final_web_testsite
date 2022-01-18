LOL 승률 예측
======
### 🎡챔피언의 조합과 최근 유저 승률을 분석하여 게임 승률을 예측한다🎡
#### #인공지능 #딥러닝 #롤 #크롤링 #웹 #op.gg
<!-- <img src="https://user-images.githubusercontent.com/90249177/148031177-748fb2dc-1626-42b5-aad4-543357d7d010.png" width="100%" height="60%" title="Pokemon" alt="Pokemon"></img> -->

## Abstract
 ### - CS.GG 웹 사이트의 기능에 대한 간략 설명입니다.</p>
 기능 1: 플레이 하고 있는 유저명을 입력해서 인게임 정보를 불러와 딥러닝 기술을 통해 승률을 예측합니다.</p>
 기능 2: 챔피온 10개를 입력해서 해당 챔피온으로 게임을 딥러닝 기술을 통해 이길 확률을 예측합니다.</p>
 기능 3: CS.GG 웹 사이트에서 로그인과 로그아웃 등을 통해 활동이 가능합니다.</p>
 Step 4: CS.GG 웹 사이트에서 게시판 기능을 활용하여 글을 작성합니다.</p>

## Technology
<ul>
  <li>Artificial Intelligenc -> Deep Learning -> Neural Network</li>
  <li>Data -> Crawling -> OP.GG</li>
  <li>Front-End -> Html, Css, Javascript </li>
  <li>Back-End -> Django, djangorestframework </li>
</ul>

## Deep Learning
승률예측을 하기 위해서 input으로 받은 인자는, 상대편 우리편 챔피언 10개의 값과 각 유저의 승률 10개 총 20개의 데이터 받았다.
각 챔피언들의 이름은 자연수 값으로 매핑되어있고, 승률은 승률 그대로 받아서 numpy array에 값을 넣었다.
가장 일반적인 3-layer NN으로 학습이 가능하다고 판단하여서 Keras tool을 이용하여 모델링을 하였다.
```python

model = Sequential()
model.add(Dense(32, activation = 'relu', input_shape= (20,)))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(2, activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.summary()
model.fit(x,y,epochs = 15)
```
Train data set은 16000개 이고 15 epochs로 학습을 진행하였다.
output에 softmax를 적용한뒤 crossentropy의 미분을 사용하여 나온 gradient 값의 미분값을 통해 weight 값들을 update 시켜나갔다.


## Data
Crawling 기술을 활용해서 데이터 수집을 진행했다.
언어는 Python을 사용해서 데이터를 가져올 수 있도록 했다.
Python에서 BeatifulSoup와 Selenium 모듈을 활용해서 Crawling을 진행했다.
Crawling은 op.gg 사이트에서 진행했으며 챔피온 조합을 가져올 수 있도록 했다.
데이터는 10X1 행렬 16843개와 20X1 행렬 868개를 수집했다.
해당 데이터로 딥러닝이 학습하도록 실행했다.


## Back-End
Django와 sqlite를 이용하여 서버와 데이터 베이스를 구축하였다.
AbstractUser class를 import하여 로그인, 회원가입 그리고 게시판에 글쓰는 기능을 구현하였다.

## Details
<ul>
  <li>Neural Network </li>
  <li>Crawling: Python(BeautifulSoup & Selenium), Site(op.gg), Dataset -> 16843개(10*1), 868개(20*1)</li>
  <li>Data Structure: 10*1(Champion / Result), 20*1(Champion, Win Rate / Result) </li>
  <li>Front-End -> Bootstrap template 활용, op.gg 및 fow.kr 디자인 참고, front-back 통신에 jquery활용</li>
  <li>Back-End -> Keras 를 이용한 3-layer nn 모델을 만들어서 15 epoch 16843개의 dataset를 학습시킴</li>
</ul>

## Contributers
- [장준형](https://github.com/JunHyungJang)
- [박정웅](https://github.com/yeolia327)
- [김수민](https://github.com/SeanKim37)
