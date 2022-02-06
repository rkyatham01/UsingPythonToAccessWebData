import urllib.error
import urllib.request
import urllib.parse
import json
import ssl

aimingfor = "http://py4e-data.dr-chuck.net/json?"

location = input("Enter location: ")

if len(location) < 1:
    location = "Kyiv Polytechnical Institute"

url = aimingfor + urllib.parse.urlencode({"address": location, "key" : 42}) #mering the 2 urls so we parse the name inputted or location
#key = 42 is a key that is
print("Retrieving",url)
#Now you would see get data

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

datanow = urllib.request.urlopen(url,context=ctx)
datanow = datanow.read()

print("Retrieved",len(datanow),"characters") # of characters in it

js = json.loads(datanow) #now js is in json form

print(js["results"][0]["place_id"])
