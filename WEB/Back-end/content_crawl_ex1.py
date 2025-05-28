from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.goto80.com/the-demoscene-as-a-unesco-heritage-in-sweden")

soup = BeautifulSoup(response.text, 'html.parser')

contents = soup.select("div.entry-content > p")

for idx in contents:
    content = idx.get_text()
    print(content)