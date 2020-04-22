import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("https://beatest.in/api/v0.1/colleges")

counts = dict()
for line in fhand:
	words = line.decode().strip()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print(counts)

# count the frequency of character in web page