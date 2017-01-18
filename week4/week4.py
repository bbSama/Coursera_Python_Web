import urllib
from bs4 import *

def Parse(url):
    print "Retrieving: "+url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,'lxml')
    return soup('a')[position-1].get('href',None)

url = raw_input("Enter URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))
url = Parse(url)
for x in range(count):
    url = Parse(url)
