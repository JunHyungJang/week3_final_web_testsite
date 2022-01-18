from bs4 import BeautifulSoup
from selenium import webdriver
import urllib

hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}

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
    '워윅': 101, '유미': 102, '이렐리아': 103, '이블린': 104, '이즈리얼': 105, '일라오이': 106, '자르반 4세': 107, '자야': 108, '자이라': 109,
    '자크': 110,
    '잔나': 111, '잭스': 112, '제드': 113, '제라스': 114, '제이스': 115, '조이': 116, '직스': 117, '진': 118, '질리언': 119, '징크스': 120,
    '초가스': 121, '카르마': 122, '카밀': 123, '카사딘': 124, '카서스': 125, '카시오페아': 126, '카이사': 127, '카직스': 128, '카타리나': 129,
    '칼리스타': 130,
    '케넨': 131, '케이틀린': 132, '케인': 133, '케일': 134, '코그모': 135, '코르키': 136, '퀸': 137, '클레드': 138, '키아나': 139, '킨드레드': 140,
    '타릭': 141, '탈론': 142, '탈리야': 143, '탐 켄치': 144, '트런들': 145, '트리스타나': 146, '트린다미어': 147, '트위스티드 페이트': 148, '트위치': 149,
    '티모': 150,
    '파이크': 151, '판테온': 152, '피들스틱': 153, '피오라': 154, '피즈': 155, '하이머딩거': 156, '헤카림': 157
}

ImgList = ['https://opgg-static.akamaized.net/images/lol/champion/Garen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Galio.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gangplank.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gragas.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Graves.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gwen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Gnar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nami.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nasus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nautilus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nocturne.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nunu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Nidalee.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Neeko.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Darius.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Diana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Draven.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ryze.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rakan.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rammus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lux.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rumble.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Renekton.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Leona.png',
 'https://opgg-static.akamaized.net/images/lol/champion/RekSai.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rell.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Rengar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lucian.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lulu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Leblanc.png',
 'https://opgg-static.akamaized.net/images/lol/champion/LeeSin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Riven.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lissandra.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Lillia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/MasterYi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Maokai.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Malzahar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Malphite.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Mordekaiser.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Morgana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/DrMundo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/MissFortune.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Bard.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Varus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Veigar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vayne.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vex.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Velkoz.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Volibear.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Braum.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Brand.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Vladimir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Blitzcrank.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Viego.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Viktor.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Poppy.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Samira.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sion.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sylas.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shaco.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Senna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Seraphine.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sejuani.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sett.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sona.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Soraka.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Shyvana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Swain.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Skarner.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Sivir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/XinZhao.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Syndra.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Singed.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Thresh.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ahri.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Amumu.png',
 'https://opgg-static.akamaized.net/images/lol/champion/AurelionSol.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ivern.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Azir.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Akali.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Akshan.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Aatrox.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Aphelios.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Alistar.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Annie.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Anivia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ashe.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yasuo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ekko.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Elise.png',
 'https://opgg-static.akamaized.net/images/lol/champion/MonkeyKing.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ornn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Orianna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Olaf.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yone.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yorick.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Udyr.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Urgot.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Warwick.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Yuumi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Irelia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Evelynn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ezreal.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Illaoi.png',
 'https://opgg-static.akamaized.net/images/lol/champion/JarvanIV.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Xayah.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zyra.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zac.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Janna.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jax.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zed.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Xerath.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jayce.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zoe.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Ziggs.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jhin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Zilean.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Jinx.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Chogath.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Karma.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Camille.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kassadin.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Karthus.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Cassiopeia.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kaisa.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Khazix.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Katarina.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kalista.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kennen.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Caitlyn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kayn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kayle.png',
 'https://opgg-static.akamaized.net/images/lol/champion/KogMaw.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Corki.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Quinn.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kled.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Qiyana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Kindred.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Taric.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Talon.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Taliyah.png',
 'https://opgg-static.akamaized.net/images/lol/champion/TahmKench.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Trundle.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Tristana.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Tryndamere.png',
 'https://opgg-static.akamaized.net/images/lol/champion/TwistedFate.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Twitch.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Teemo.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Pyke.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Pantheon.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fiddlesticks.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fiora.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Fizz.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Heimerdinger.png',
 'https://opgg-static.akamaized.net/images/lol/champion/Hecarim.png']


# def live(liveUser):
#     print("live start")
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
#     liveName = urllib.parse.quote(liveUser)
#     liveUrl = "https://www.op.gg/summoner/userName=" + liveName + "?l=ko_KR"
#     driver.get(liveUrl)
#     driver.find_element_by_css_selector('.SpectateTabButton').click()
#     check = 0
#     namename = list()
#     winwin = list()
#     champchamp = list()
#     while True:
#         liveHtml = driver.page_source
#         liveSoup = BeautifulSoup(liveHtml, "html.parser")
#         loading = liveSoup.find_all("a", attrs={"class": "SummonerName"})
#         print(check)
#         check += 1
#         if check >= 5:
#             print("현재 게임 중이 아닙니다!")
#             return False
#         if len(loading) != 0:
#             break

#     for i in range(len(loading)):
#         playingName = loading[i].text.strip()
#         namename.append(playingName)

#     rate = liveSoup.find_all("span", attrs={"class": "Ratio"})
#     for j in range(0, len(rate)):
#         if len(rate[j]["class"]) > 1:
#             playingRate = rate[j].text.strip()
#             if str(playingRate) == "0%":
#                 playingRate = "50%"
#             playingRate = playingRate[0:len(playingRate) - 1]
#             if playingRate.isdigit() != True:
#                 playingRate = 50
#             winwin.append(int(playingRate))

#     champion = liveSoup.find_all("a", attrs={"class": "Image tip"})
#     for k in range(len(champion)):
#         playingChamp = champion[k]["title"]
#         champchamp.append(lolChampion[playingChamp])

#     Container = {}

#     Container['Names'] = namename
#     Container['Winrate'] = winwin
#     Container['Champions'] = champchamp

#     Container['Champion Images'] = []
#     for i in range(len(Container['Champions'])):
#         Container['Champion Images'].append(ImgList[Container["Champions"][i]])

#     return Container


def getGameData20(name):
    # Container = live(name)

    print("getGameData20")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    liveName = urllib.parse.quote(name)
    liveUrl = "https://www.op.gg/summoner/userName=" + liveName + "?l=ko_KR"
    driver.get(liveUrl)
    driver.find_element_by_css_selector('.SpectateTabButton').click()
    check = 0
    namename = list()
    winwin = list()
    champchamp = list()
    while True:
        liveHtml = driver.page_source
        liveSoup = BeautifulSoup(liveHtml, "html.parser")
        loading = liveSoup.find_all("a", attrs={"class": "SummonerName"})
        print(check)
        check += 1
        if check >= 5:
            print("현재 게임 중이 아닙니다!")
            return False
        if len(loading) != 0:
            break

    for i in range(len(loading)):
        playingName = loading[i].text.strip()
        namename.append(playingName)

    rate = liveSoup.find_all("span", attrs={"class": "Ratio"})
    for j in range(0, len(rate)):
        if len(rate[j]["class"]) > 1:
            playingRate = rate[j].text.strip()
            if str(playingRate) == "0%":
                playingRate = "50%"
            playingRate = playingRate[0:len(playingRate) - 1]
            if playingRate.isdigit() != True:
                playingRate = 50
            winwin.append(int(playingRate))

    champion = liveSoup.find_all("a", attrs={"class": "Image tip"})
    for k in range(len(champion)):
        playingChamp = champion[k]["title"]
        champchamp.append(lolChampion[playingChamp])

    Container = {}

    Container['Names'] = namename
    Container['Winrate'] = winwin
    Container['Champions'] = champchamp

    Container['Champion Images'] = []
    for i in range(len(Container['Champions'])):
        Container['Champion Images'].append(ImgList[Container["Champions"][i]])

    print("getGameData20 end")


    return Container