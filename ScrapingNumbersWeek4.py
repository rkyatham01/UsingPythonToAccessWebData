import urllib.request
import urllib.parse
import urllib.error #import these, this is a library inbuilt closer to Sockets end points
import ssl #For certificate errors that you ignore
from bs4 import BeautifulSoup #imports Beautiful soup
import re #Regex Expressions

ctx = ssl.create_default_context() #creates a default object for ssl so it bypasses encryption and sets it to default
ctx.check_hostname = False #checks if host name is false
ctx.verify_mode = ssl.CERT_NONE #Puts the mode in ignoring Certificate errors

url = input("Enter url : ")
if (len(url) < 1):
    url = "http://py4e-data.dr-chuck.net/comments_1471056.html" #file its going to use as sample data

html = urllib.request.urlopen(url, context=ctx).read() #The context=ctx is neded with the ^^^ so that it can skip the encryption layers
#html is basically like a file hdnlr in this case bc its been read()
parseddoc = BeautifulSoup(html,"html.parser")
#parseddoc is a parseddoc here
#Retrieve tags
tags = parseddoc("span") #gets all the span tags from the parsed document
sum = 0

for tag in tags: #trying to get the numbers only to add them up together
    x = tag.contents[0] #Gets the first contents of the span tag
    sum = sum + int(x)

print(sum)