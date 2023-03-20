
from bs4 import BeautifulSoup
import requests
def web():
    
    header = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }
    url = "https://search.crossref.org/?q=web+progam&from_ui=yes"
    req = requests.get(url,headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.find('table')
    for i in items.findAll("td"):
        a= i.find('p','lead')
        b= i.find('div','item-links-outer')
        c= b.find('div','item-links')
        d= c.find('a')
        print(a.text)
        print(d.text)
web()

 