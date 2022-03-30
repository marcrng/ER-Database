import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
page = requests.get(URL)
print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")
# Find first item name
first_name = soup.findAll('a')[39].text
names = soup.findAll('a')

initial = []

# Build iteration to extract all item names from first page
for txt in names[39:64]:
    initial.append(txt.getText())
    print(txt.getText())

# Expand iteration to include all item pages (2-66)
for i in range(2, 67):
    URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
    pagenum = "&wpv_paged=" + str(i)
    page = requests.get(URL + pagenum)

    soup = BeautifulSoup(page.content, "html.parser")
    # Find first item name
    first_name = soup.findAll('a')[39].text
    names = soup.findAll('a')
    for txt in names[39:64]:
        initial.append(txt.getText())
        print(txt.getText())

dfName = pd.DataFrame({
    "item_name": initial
})

# Export dataframe to csv
dfName.to_csv('initialNames.csv')
