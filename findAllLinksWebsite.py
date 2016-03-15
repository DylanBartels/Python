# Require's beautifulsoup3
import urllib
from BeautifulSoup import *

url = raw_input('Enter url to analyse: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)