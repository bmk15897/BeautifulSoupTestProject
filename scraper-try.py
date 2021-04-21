import requests

from bs4 import BeautifulSoup

#page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
#print(page.content)
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
#html = list(soup.children)[2]
#print(list(list(html.children)[1].children)[1].get_text())
#print(soup.find_all('p')[0].get_text())


#page1 = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
#print(page.content)
#soup1 = BeautifulSoup(page1.content, 'html.parser')
#print(soup1.find_all('p', class_='outer-text'))
#print(soup1.find_all(id="first"))
#print(soup1.select("div p"))