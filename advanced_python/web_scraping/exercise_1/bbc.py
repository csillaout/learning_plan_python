import requests
from bs4 import BeautifulSoup
#python env: python3 -m venv venv
#activate: source venv/bin/activate
#requests and beautiful soup: pip install requests beautifulsoup4

#fetch the webpage
url = "https://bbc.com/news"
response = requests.get(url)

#parese the html content
soup = BeautifulSoup(response.text, 'html.parser')

#extract headline
headlines = soup.find_all('a')

print("BBC News Headlines:")
for idx, headline in enumerate(headlines[:10]): #limit to the first 10 headlines
    print(f"{idx + 1}. {headline.get_text(strip=True)}")
