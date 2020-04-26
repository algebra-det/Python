import requests

# it will open a authentication popup too, to confirm the user credentials
# these are some features you will use in other websites too

# We have to pass 'auth' instead of 'params' or 'data'
response = requests.get("https://httpbin.org/basic-auth/corey/testing", auth=('corey', 'testing'))

"""
As we have passed the right credentials as in the url , we will get TRUE response [200] i.e. authorized,
but if we don't pass the correct credentials than it will result in [401] i.e. unauthorized
"""

print response


"""
One more thing:
If we run requests, than it will wait until we get a requests,
and it will wait and hang forever 
SO to overcome this issue we should :

Set a timeout in our code
"""
