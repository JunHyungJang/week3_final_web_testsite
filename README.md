LOL ์น๋ฅ  ์์ธก
======
### ๐ก์ฑํผ์ธ์ ์กฐํฉ๊ณผ ์ต๊ทผ ์ ์  ์น๋ฅ ์ ๋ถ์ํ์ฌ ๊ฒ์ ์น๋ฅ ์ ์์ธกํ๋ค๐ก
#### #์ธ๊ณต์ง๋ฅ #๋ฅ๋ฌ๋ #๋กค #ํฌ๋กค๋ง #์น #op.gg
<!-- <img src="https://user-images.githubusercontent.com/90249177/148031177-748fb2dc-1626-42b5-aad4-543357d7d010.png" width="100%" height="60%" title="Pokemon" alt="Pokemon"></img> -->

## Abstract
 ### - CS.GG ์น ์ฌ์ดํธ์ ๊ธฐ๋ฅ์ ๋ํ ๊ฐ๋ต ์ค๋ช์๋๋ค.</p>
 ๊ธฐ๋ฅ 1: ํ๋ ์ด ํ๊ณ  ์๋ ์ ์ ๋ช์ ์๋ ฅํด์ ์ธ๊ฒ์ ์ ๋ณด๋ฅผ ๋ถ๋ฌ์ ๋ฅ๋ฌ๋ ๊ธฐ์ ์ ํตํด ์น๋ฅ ์ ์์ธกํฉ๋๋ค.</p>
 ๊ธฐ๋ฅ 2: ์ฑํผ์จ 10๊ฐ๋ฅผ ์๋ ฅํด์ ํด๋น ์ฑํผ์จ์ผ๋ก ๊ฒ์์ ๋ฅ๋ฌ๋ ๊ธฐ์ ์ ํตํด ์ด๊ธธ ํ๋ฅ ์ ์์ธกํฉ๋๋ค.</p>
 ๊ธฐ๋ฅ 3: CS.GG ์น ์ฌ์ดํธ์์ ๋ก๊ทธ์ธ๊ณผ ๋ก๊ทธ์์ ๋ฑ์ ํตํด ํ๋์ด ๊ฐ๋ฅํฉ๋๋ค.</p>
 Step 4: CS.GG ์น ์ฌ์ดํธ์์ ๊ฒ์ํ ๊ธฐ๋ฅ์ ํ์ฉํ์ฌ ๊ธ์ ์์ฑํฉ๋๋ค.</p>

## Technology
<ul>
  <li>Artificial Intelligenc -> Deep Learning -> Neural Network</li>
  <li>Data -> Crawling -> OP.GG</li>
  <li>Front-End -> Html, Css, Javascript </li>
  <li>Back-End -> Django, djangorestframework </li>
</ul>

## Deep Learning
์น๋ฅ ์์ธก์ ํ๊ธฐ ์ํด์ input์ผ๋ก ๋ฐ์ ์ธ์๋, ์๋ํธ ์ฐ๋ฆฌํธ ์ฑํผ์ธ 10๊ฐ์ ๊ฐ๊ณผ ๊ฐ ์ ์ ์ ์น๋ฅ  10๊ฐ ์ด 20๊ฐ์ ๋ฐ์ดํฐ ๋ฐ์๋ค.
๊ฐ ์ฑํผ์ธ๋ค์ ์ด๋ฆ์ ์์ฐ์ ๊ฐ์ผ๋ก ๋งคํ๋์ด์๊ณ , ์น๋ฅ ์ ์น๋ฅ  ๊ทธ๋๋ก ๋ฐ์์ numpy array์ ๊ฐ์ ๋ฃ์๋ค.
๊ฐ์ฅ ์ผ๋ฐ์ ์ธ 3-layer NN์ผ๋ก ํ์ต์ด ๊ฐ๋ฅํ๋ค๊ณ  ํ๋จํ์ฌ์ Keras tool์ ์ด์ฉํ์ฌ ๋ชจ๋ธ๋ง์ ํ์๋ค.
```python

model = Sequential()
model.add(Dense(32, activation = 'relu', input_shape= (20,)))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(2, activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.summary()
model.fit(x,y,epochs = 15)
```
Train data set์ 16000๊ฐ ์ด๊ณ  15 epochs๋ก ํ์ต์ ์งํํ์๋ค.
output์ softmax๋ฅผ ์ ์ฉํ๋ค crossentropy์ ๋ฏธ๋ถ์ ์ฌ์ฉํ์ฌ ๋์จ gradient ๊ฐ์ ๋ฏธ๋ถ๊ฐ์ ํตํด weight ๊ฐ๋ค์ update ์์ผ๋๊ฐ๋ค.


## Data
Crawling ๊ธฐ์ ์ ํ์ฉํด์ ๋ฐ์ดํฐ ์์ง์ ์งํํ๋ค.
์ธ์ด๋ Python์ ์ฌ์ฉํด์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ฌ ์ ์๋๋ก ํ๋ค.
Python์์ BeatifulSoup์ Selenium ๋ชจ๋์ ํ์ฉํด์ Crawling์ ์งํํ๋ค.
Crawling์ op.gg ์ฌ์ดํธ์์ ์งํํ์ผ๋ฉฐ ์ฑํผ์จ ์กฐํฉ์ ๊ฐ์ ธ์ฌ ์ ์๋๋ก ํ๋ค.
๋ฐ์ดํฐ๋ 10X1 ํ๋ ฌ 16843๊ฐ์ 20X1 ํ๋ ฌ 868๊ฐ๋ฅผ ์์งํ๋ค.
ํด๋น ๋ฐ์ดํฐ๋ก ๋ฅ๋ฌ๋์ด ํ์ตํ๋๋ก ์คํํ๋ค.


## Back-End
Django์ sqlite๋ฅผ ์ด์ฉํ์ฌ ์๋ฒ์ ๋ฐ์ดํฐ ๋ฒ ์ด์ค๋ฅผ ๊ตฌ์ถํ์๋ค.
AbstractUser class๋ฅผ importํ์ฌ ๋ก๊ทธ์ธ, ํ์๊ฐ์ ๊ทธ๋ฆฌ๊ณ  ๊ฒ์ํ์ ๊ธ์ฐ๋ ๊ธฐ๋ฅ์ ๊ตฌํํ์๋ค.

## Details
<ul>
  <li>Neural Network </li>
  <li>Crawling: Python(BeautifulSoup & Selenium), Site(op.gg), Dataset -> 16843๊ฐ(10*1), 868๊ฐ(20*1)</li>
  <li>Data Structure: 10*1(Champion / Result), 20*1(Champion, Win Rate / Result) </li>
  <li>Front-End -> Bootstrap template ํ์ฉ, op.gg ๋ฐ fow.kr ๋์์ธ ์ฐธ๊ณ , front-back ํต์ ์ jqueryํ์ฉ</li>
  <li>Back-End -> Keras ๋ฅผ ์ด์ฉํ 3-layer nn ๋ชจ๋ธ์ ๋ง๋ค์ด์ 15 epoch 16843๊ฐ์ dataset๋ฅผ ํ์ต์ํด</li>
</ul>

## Contributers
- [์ฅ์คํ](https://github.com/JunHyungJang)
- [๋ฐ์ ์](https://github.com/yeolia327)
- [๊น์๋ฏผ](https://github.com/SeanKim37)
