import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Enter url')
data = urllib.request.urlopen(url).read()

soup = BeautifulSoup(data,'html.parser')

# Retrieve all anchor tags

anchor_tag = soup('a');

for tag in anchor_tag:
    print(tag.get('href',None))

# for tag in anchor_tag:
#     print(tag.get('href',None))

