import requests
from bs4 import BeautifulSoup

import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")



html = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States")

bsObj = BeautifulSoup(html.content, "html.parser")


all_tables = bsObj.find_all('table', class_ ='wikitable')[0]

f = open('NITEESHA.txt', 'a', encoding="utf-8")
y = all_tables.findAll('tr')[2:]

j = 1
for tr in y:
    print(f"{j} State - {tr.th.a.string}")
    f.write(f"{j} State - {tr.th.a.string}")
    z = tr.findAll('td')
    columnsize = len(z)
    j = j+1
    print(z[0].text)
    print(f"   Capital -{z[1].text}")
    f.write(f"   Capital -{z[1].text}")