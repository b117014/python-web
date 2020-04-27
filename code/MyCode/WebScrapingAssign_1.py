import urllib.request,urllib.error,urllib.parse;
from bs4 import BeautifulSoup

data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_396139.html').read()

soup = BeautifulSoup(data,'html.parser')

span_tag = soup('span')
sum=0
for tag in span_tag:
    sum+=int(tag.contents[0])      

print(sum)