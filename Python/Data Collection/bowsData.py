import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

URL = "https://eldenring.wiki.fextralife.com/Bows"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Create lists for necessary columns
name = []
atkPhysical = []
defPhysical = []
range = []
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

for i in soup.findAll('tr')[1:8]:
    tds = i.findAll('td')

    name.append(tds[0].text.strip())
    atkPhysical.append(tds[1].text.strip().split(' ', 1)[0])
    defPhysical.append(tds[1].text.strip().split(' ', 1)[1])
    range.append(tds[2].text.strip())
    atkMagic.append(tds[3].text.strip().split(' ', 1)[0])
    defMagic.append(tds[3].text.strip().split(' ', 1)[1])
    atkFire.append(tds[4].text.strip().split(' ', 1)[0])
    defFire.append(tds[4].text.strip().split(' ', 1)[1])
    atkLight.append(tds[5].text.strip().split(' ', 1)[0])
    defLight.append(tds[5].text.strip().split(' ', 1)[1])
    atkHoly.append(tds[6].text.strip().split(' ', 1)[0])
    try:
        defHoly.append(tds[6].text.strip().split(' ', 1)[1])
    except:
        defHoly.append('-')
    crit.append(tds[7].text.strip().split(' ', 1)[0])
    guardBoost.append(tds[7].text.strip().split(' ', 1)[1])
    strReq.append(tds[8].text.strip().split(' ', 1)[0])
    strScaling.append(tds[8].text.strip().split(' ', 1)[1])
    dexScaling.append(tds[9].text.strip().split(' ', 1)[0])
    try:
        dexReq.append(tds[9].text.strip().split(' ', 1)[1])
    except:
        dexReq.append('-')
    intScaling.append(tds[10].text.strip().split(' ', 1)[0])
    try:
        intReq.append(tds[10].text.strip().split(' ', 1)[1])
    except:
        intReq.append('-')
    faiScaling.append(tds[11].text.strip().split(' ', 1)[0])
    try:
        faiReq.append(tds[11].text.strip().split(' ', 1)[1])
    except:
        faiReq.append('-')
    arcScaling.append(tds[12].text.strip().split(' ', 1)[0])
    arcReq.append(tds[12].text.strip().split(' ', 1)[1])
    weight.append(tds[13].text.strip())
    skill.append(re.sub('[^a-zA-Z]+', '', tds[14].text.strip()))


df = pd.DataFrame({
    'name': name,
    'atkPhysical': atkPhysical,
    'defPhysical': defPhysical,
    'range': range,
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

df.to_csv('bowsData.csv')
