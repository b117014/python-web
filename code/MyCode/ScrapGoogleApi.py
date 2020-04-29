import json
import urllib.request,urllib.parse,urllib.error;

url = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input('Enter Location')
    if len(address)<1 : break;
    print(urllib.parse.urlencode({'address':address}))
    url_ = url + urllib.parse.urlencode({'address':address})

    print('retrieving', url_)
    uh =urllib.request.urlopen(url_)
    data = uh.read().decode()
    print("data" ,data)
    try:
        js = json.loads(data)
    except:
        js =None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure Tor Retrieve')
        print(data)
        continue
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print("lat", lat, "long", lng)
    location = js['results'][0]['formatted_address']
    print(location)