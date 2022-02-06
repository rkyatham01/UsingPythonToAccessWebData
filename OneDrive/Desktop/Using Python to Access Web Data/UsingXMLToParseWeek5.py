import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET #Et is the handle or shortcut to the imported Tree

import ssl # To get past the website check
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE #order matters

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1471058.xml"
print("Retrieving:" + url)

xmlfile = urllib.request.urlopen(url,context=ctx).read()
print("Retrieved :", len(xmlfile),"characters")

tree = ET.fromstring(xmlfile) #converts fromstring to a list
#a tree is made now to search through the XML

lst = tree.findall("comments/comment/count") #dig through the file
print("Count:", len(lst))

sum = 0 #adds to this sum
for every in lst:
    sum = sum + int(every.text)

print(sum)



