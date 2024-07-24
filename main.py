import requests
from bs4 import BeautifulSoup

url = "example url"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headings = soup.find_all('h1')
for heading in headings:
    print(heading.text)

# Find all images with a src attribute
images = soup.find_all('img', {'src': True})
for image in images:
    print(f"Image source: {image['src']}")

# Find the first div with class "special" and its text
special_div = soup.find('div', class_='special')
if special_div:
    print(f"Special div text: {special_div.get_text()}")