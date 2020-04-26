import requests

# It's a url of an image file
response = requests.get("https://imgs.xkcd.com/comics/python.png")

# To print out the content is not a good idea as it will return the data in bits
# print response.content

# so we should do instead
# We will create a file which will contain the image from the response
with open("comic.png", "wb") as f:          # 'wb' means write bytes
    f.write(response.content)
