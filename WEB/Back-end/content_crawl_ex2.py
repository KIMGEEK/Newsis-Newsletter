from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.science.org/content/blog-post/things-i-won-t-work-dioxygen-difluoride") # 43533496

soup = BeautifulSoup(response.text, 'html.parser')
contents = soup.find('div')
print(contents)
#for idx in contents:
#    content = idx.get_text()
#    print(content)