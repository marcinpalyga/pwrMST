import webbrowser
from bs4 import BeautifulSoup
import requests

def wikipedia():
    page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    content = page.content
    url = page.url
    soup = BeautifulSoup(content, 'html.parser')
    title = str(soup.find_all('title'))
    print(title)
    answer = input("Do you like the title of that page? ").upper()
    if answer == 'Y':
        webbrowser.open(url)
        return "Page is open in your browser"
    else:
       wikipedia()
       return "Page is open in your browser"

print(wikipedia())