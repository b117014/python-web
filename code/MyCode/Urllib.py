import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("https://beatest.in/api/v0.1/colleges")

for line in fhand:
	print(line.decode())