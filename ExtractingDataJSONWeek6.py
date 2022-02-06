import json
import ssl

import urllib.parse
import urllib.request
import urllib.error

url = input("Enter file name")

if (len(url) < 1):
    url = "http://py4e-data.dr-chuck.net/comments_1471059.json"

print("Enter location", url)
print("Retrieved",url)
cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE

file = urllib.request.urlopen(url, context=cxt)
data = (file.read()).decode() #Decodes from byte to String

info = json.loads(data) #Puts the file in JSON format after converting to string

print("Count:",len(info["comments"]))

sum = 0

for every in info["comments"]:
    sum = sum + every["count"]

print(sum)