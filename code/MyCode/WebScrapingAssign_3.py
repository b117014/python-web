import urllib, urllib.error, urllib.parse,urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_396141.xml"

data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total =0 

for count in counts:
    total+=int(count.text)
print(total)