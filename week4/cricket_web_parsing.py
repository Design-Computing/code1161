import requests
from bs4 import BeautifulSoup
url = "http://static.cricinfo.com/rss/livescores.xml"
import datetime

def get_scores():
    '''
    Print out all the latest scores.
    
    Helper function. No need to comment further
    '''
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find_all("description")
    for element in data:
        print((element.text))

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"At {now}, the latest scores are:")
get_scores()

