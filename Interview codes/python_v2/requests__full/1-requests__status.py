import requests
from requests.exceptions import HTTPError

for url in ["https://api.github.com", "https://api.github.com/invalid"]:
    try:
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as e:
        print "HTTP error occured : ",e

    except Exception as errr:
        print "Other error occured: {err}"

    else:
        print "success !"
