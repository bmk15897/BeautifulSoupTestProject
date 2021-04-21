from bs4 import BeautifulSoup
import requests

HEADER = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
link = "https://www.youtube.com/watch?v=qZp5gf9xgnE"

response = requests.get(link, headers=HEADER)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

titleSoupMeta = soup.find("meta", property="og:title")
videoTitle = titleSoupMeta["content"] if titleSoupMeta else "NotFound"

print(videoTitle) # I Will (feat. KXNG Crooked, Royce da 5'9" & Joell Ortiz) [Official Audio]
