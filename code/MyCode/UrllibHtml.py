import urllib.request, urllib.parse, urllib.error

handf = urllib.request.urlopen("http://dr-chuck.com/page1.htm")

for line in handf:
	print(line.decode())