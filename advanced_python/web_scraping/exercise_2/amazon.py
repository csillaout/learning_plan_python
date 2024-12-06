#python env: python3 -m venv venv
#activate: source venv/bin/activate
#requests and beautiful soup: pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[0]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles) 
import pandas as pd
print(pd.__version__)
df = pd.DataFrame(columns = world_table_titles)
df
