import urllib.request,urllib.error,urllib.parse;
from bs4 import BeautifulSoup

pos = int(input('Position - '))
loop = int(input('Times - '))
url = input("Enter - ")

for ct in range(loop):
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data,'html.parser')
    tag = soup('a')
    new_url = tag[pos-1].get('href',None)
    url = new_url
    name = tag[pos-1].contents[0]

print(name)