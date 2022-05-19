import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

URL = "https://eldenring.wiki.fextralife.com/Axes"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
