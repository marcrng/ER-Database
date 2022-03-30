import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
page = requests.get(URL)
print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")

# Create list for names, category
name = []
category = []

# Create dict for name and category for page 1
for i in soup.findAll('tr')[1:]:
    tds = i.find_all('td')

    name.append(tds[0].text.strip())
    category.append(tds[1].text.strip())

# Create dict, name for other pages
for i in range(2, 67):
    URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
    pagenum = "&wpv_paged=" + str(i)
    page = requests.get(URL + pagenum)

    soup = BeautifulSoup(page.content, "html.parser")
    # Find first item name
    first_name = soup.findAll('a')[39].text
    names = soup.findAll('a')
    for i in soup.findAll('tr')[1:]:
        tds = i.find_all('td')

        name.append(tds[0].text.strip())
        category.append(tds[1].text.strip())

df = pd.DataFrame({
    "itemName": name,
    "itemType": category
})

df.to_csv('namesType.csv')


# Insert item info for each weapon and armor
