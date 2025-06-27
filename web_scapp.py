import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print("scrapping 'https://en.wikipedia.org/wiki/Python_(programming_language)' : ")
print(f" status code : {r.status_code}")
print("_________")

soup = BeautifulSoup(r.content, 'html.parser')
web_title = soup.find('title')
print(f"title of this web page is : {web_title.text}")
print("_________")

web_classes = soup.find_all(class_="vector-toc-text")
# print(web_class)
for web_class in web_classes:
    print(f" class : {web_class.text}")
print("_________")

img_python = soup.find_all("img", class_="mw-file-element")
for img in img_python:
    print(f" img : {img['src']}")

print("_________")