from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup

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


def renewalOPGG(Name):
    print("갱신중")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
    url = 'https://www.op.gg/summoner/userName=' + Name
    action = ActionChains(driver)
    driver.get(url)

    try:
        driver.find_element_by_css_selector('.Button.SemiRound.Blue').click()
        action.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get_screenshot_as_file('opgg.png')
    except Exception as ex:
        print("exception: ", ex)
        print("갱신완료")
        driver.quit()
    print("갱신완료")
    driver.quit()


def ingameOPGG(Name):
    print("분석중")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    url = 'https://www.op.gg/summoner/userName=' + Name

    driver.set_page_load_timeout(50)
    driver.get(url)
    Container = {}

    driver.find_element_by_css_selector('.SpectateTabButton').click()
    time.sleep(30)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find("link").attrs['href']

    Container['Link'] = link

    ingameInfo = soup.find("div", {"class": "tabItem Content SummonerLayoutContent summonerLayout-spectator"})

    names = ingameInfo.find_all("td", {"class": "SummonerName Cell"})
    Container['Names'] = []

    if len(names) == 0:
        return Container

    for name in names:
        Container['Names'].append(name.text.strip())

    champions = ingameInfo.find_all("td", {"class": "ChampionImage Cell"})
    Container['Champions'] = []
    for champion in champions:
        champ = str(champion.find("a").attrs['href'])
        champ = champ.replace("/champion/", '').replace("/statistics", '').capitalize()
        Container['Champions'].append(champ)

    tiers = ingameInfo.find_all("td", {"class": "CurrentSeasonTierRank Cell"})
    Container['Tiers'] = []
    for tier in tiers:
        Container['Tiers'].append(tier.text.strip())

    ratios = ingameInfo.find_all("td", {"class": "RankedWinRatio Cell"})
    Container['Ratios'] = []
    for ratio in ratios:
        Container['Ratios'].append(ratio.text.replace('\n', '').replace('\t', '').strip())

    champRatios = ingameInfo.find_all("td", {"class": "ChampionInfo Cell"})
    Container['Champion Ratios'] = []
    for champRatio in champRatios:
        Container['Champion Ratios'].append(
            champRatio.text.replace(' ', '').replace('\n', '').replace('\t', '').strip())

    Container['Champion Images'] = []
    for i in range(len(Container['Champions'])):
        Container['Champion Images'].append(ImgList[champion_name.index(Container['Champions'][i])])

    driver.quit()

    return Container