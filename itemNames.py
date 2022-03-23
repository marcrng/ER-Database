import requests
from bs4 import BeautifulSoup

URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# Find first item name
first_name = soup.findAll('a')[39].text
names = soup.findAll('a')

# Build iteration to extract all item names from first page
for txt in names[39:64]:
    print(txt.getText())

# Expand iteration to include all item pages (2-66)
for i in range(2, 66):
    URL = "https://eip.gg/elden-ring/search/?wpv_aux_current_post_id=85703&wpv_aux_parent_post_id=85703&wpv_view_count=85707"
    pagenum = "&wpv_paged=" + str(i)
    page = requests.get(URL + pagenum)

    soup = BeautifulSoup(page.content, "html.parser")
    # Find first item name
    first_name = soup.findAll('a')[39].text
    names = soup.findAll('a')
    for txt in names[39:64]:
        print(txt.getText())
