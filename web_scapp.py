import requests
from bs4 import BeautifulSoup
import cssutils

r = requests.get("https://jadi.ir/")
print("scrapping 'https://jadi.ir/' : ")
print(f" status code : {r.status_code}")
print("_________")

jadi_soup = BeautifulSoup(r.content, 'html.parser')
web_title = jadi_soup.find('title')
print(f"title of this web page is : {web_title.text}")
print("_________")

web_class = jadi_soup.find(class_='files')
print(f"one class of this web page is : {web_class.text}")
print("_________")

body_style = jadi_soup.find('body')['style']
style = cssutils.parseStyle(body_style)
print(style['background-image'])
print("_________")