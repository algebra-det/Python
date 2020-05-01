import requests

res = requests.get("http://api.letgo.com/api/iplookup.json")

res_json = res.json()
print res_json

lat = str(res_json["latitude"])
lon = str(res_json["longitude"])
print lat, lon
latlng = lat+","+ lon
print latlng

# http://maps.googleapis.com/maps/api/geocode/json?latlng=28.57,77.32&sensor=true

response = requests.post(
    "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(lat, lon),
    params={
    'sensor': 'true',
    })

print response.url
response_json = response.json()
print response_json
