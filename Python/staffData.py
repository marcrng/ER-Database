import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

URL = "https://eldenring.wiki.fextralife.com/Glintstone+Staffs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Create lists for necessary columns
name = []
atkPhysical = []
sorceryScaling = []
atkMagic = []
atkFire = []
atkLight = []
atkHoly = []
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

# Append info from webpage to lists
for i in soup.findAll('tr')[1:]:
    tds = i.findAll('td')

    name.append(tds[0].text.strip())
    atkPhysical.append(tds[1].text.strip().split(' ', 1)[0])
    sorceryScaling.append(tds[2].text.strip())
    atkMagic.append(tds[3].text.strip())
    atkFire.append(tds[4].text.strip())
    atkLight.append(tds[5].text.strip())
    atkHoly.append(tds[6].text.strip())
    crit.append(tds[7].text.strip().split(' ', 1)[0])
    guardBoost.append(tds[7].text.strip().split(' ', 1)[1])
    strReq.append(tds[8].text.strip().split(' ', 1)[0])
    strScaling.append(tds[8].text.strip().split(' ', 1)[1])
    dexReq.append(tds[9].text.strip().split(' ', 1)[0])
    # Some fields missing, if an exception is thrown, replace with -
    try:
        dexScaling.append(tds[9].text.strip().split(' ', 1)[1])
    except:
        dexScaling.append('-')
    intReq.append(tds[10].text.strip().split(' ', 1)[0])
    try:
        intScaling.append(tds[10].text.strip().split(' ', 1)[1])
    except:
        intScaling.append('-')
    faiReq.append(tds[11].text.strip().split(' ', 1)[0])
    try:
        faiScaling.append(tds[11].text.strip().split(' ', 1)[1])
    except:
        faiScaling.append('-')
    arcReq.append(tds[12].text.strip().split(' ', 1)[0])
    try:
        arcScaling.append(tds[12].text.strip().split(' ', 1)[1])
    except:
        arcScaling.append('-')
    weight.append(tds[13].text.strip())
    skill.append(re.sub('[^a-zA-Z]+', '', tds[14].text.strip()))

# Create dataframe and populate from lists
df = pd.DataFrame({
    'name': name,
    'atkPhysical': atkPhysical,
    'sorceryScaling': sorceryScaling,
    'atkMagic': atkMagic,
    'atkFire': atkFire,
    'atkLight': atkLight,
    'atkHoly': atkHoly,
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
    'weight': weight
})

df = df.replace('-', '', regex=True)

df.to_csv('staffData.csv')
