import requests, json

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# this data can also be said as A json string because of its structure
print len(response.content)
print ""

# This also converts raw data into json ...dictionary
jr = json.loads(response.content)
print len(jr)
print type(jr)

# Converts respnse into a json...dictionary
json_response = response.json()
print len(json_response)
print type(json_response)
print ""

repository = json_response['items'][0]
print repository
print type(repository)
print "Repository name: {}".format(repository['name'])
print "Repository name: {}".format(repository['description'])
