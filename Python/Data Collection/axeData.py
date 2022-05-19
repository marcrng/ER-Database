import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

URL = "https://eldenring.wiki.fextralife.com/Axes"
page = requests.get(URL)

page.content

soup = BeautifulSoup(page.content, "html.parser")

# Create lists for necessary columns
name = []
atkPhysical = []
defPhysical = []
atkMagic = []
defMagic = []
atkFire = []
defFire = []
atkLight = []
defLight = []
atkHoly = []
defHoly = []
crit = []
guardBoost = []
strReq = []
strScaling = []
dexReq = []
dexScaling = []
intReq = []
intScaling = []
faiReq = []
faiScaling = []
arcReq = []
arcScaling = []
weight = []
skill = []

for i in soup.findAll('tr')[1:14]:
    tds = i.findAll('td')

    name.append(tds[0].text.strip())
    atkPhysical.append(tds[1].text.strip().split(' ', 1)[0])
    defPhysical.append(tds[1].text.strip().split(' ', 1)[1])
    atkMagic.append(tds[2].text.strip().split(' ', 1)[0])
    defMagic.append(tds[2].text.strip().split(' ', 1)[1])
    atkFire.append(tds[3].text.strip().split(' ', 1)[0])
    defFire.append(tds[3].text.strip().split(' ', 1)[1])
    atkLight.append(tds[4].text.strip().split(' ', 1)[0])
    defLight.append(tds[4].text.strip().split(' ', 1)[1])
    atkHoly.append(tds[5].text.strip().split(' ', 1)[0])
    defHoly.append(tds[5].text.strip().split(' ', 1)[1])
    crit.append(tds[6].text.strip().split(' ', 1)[0])
    guardBoost.append(tds[6].text.strip().split(' ', 1)[1])
    strReq.append(tds[7].text.strip().split(' ', 1)[0])
    strScaling.append(tds[7].text.strip().split(' ', 1)[1])
    dexReq.append(tds[8].text.strip().split(' ', 1)[0])
    try:
        dexScaling.append(tds[8].text.strip().split(' ', 1)[1])
    except:
        dexScaling.append('-')
    intReq.append(tds[9].text.strip().split(' ', 1)[0])
    intScaling.append(tds[9].text.strip().split(' ', 1)[1])
    faiReq.append(tds[10].text.strip().split(' ', 1)[0])
    faiScaling.append(tds[10].text.strip().split(' ', 1)[1])
    arcReq.append(tds[11].text.strip().split(' ', 1)[0])
    arcScaling.append(tds[11].text.strip().split(' ', 1)[1])
    weight.append(tds[12].text.strip())
    skill.append(re.sub('[^a-zA-Z]+', '', tds[13].text.strip()))

df = pd.DataFrame({
    'name': name,
    'atkPhysical': atkPhysical,
    'defPhysical': defPhysical,
    'atkMagic': atkMagic,
    'defMagic': defMagic,
    'atkFire': atkFire,
    'defFire': defFire,
    'atkLight': atkLight,
    'defLight': defLight,
    'atkHoly': atkHoly,
    'defHoly': defHoly,
    'crit': crit,
    'guardBoost': guardBoost,
    'strReq': strReq,
    'strScaling': strScaling,
    'dexReq': dexReq,
    'dexScaling': dexScaling,
    'intReq': intReq,
    'intScaling': intScaling,
    'faiReq': faiReq,
    'faiScaling': faiScaling,
    'arcReq': arcReq,
    'arcScaling': arcScaling,
    'weight': weight,
    'skill': skill
})

df = df.replace('-', '', regex=True)

print(df)

df.to_csv('axeData.csv')
