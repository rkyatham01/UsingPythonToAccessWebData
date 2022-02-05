import ssl
import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup
#Ignore the SSL certificate error

ctx = ssl.create_default_context() #make a default context object
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE #verify mode CERT NONE

url = input("Enter url:")
count = input("Enter count:")
count = int(count)
position = input("Enter position:")
position = int(position)
keepposition = position #temporary to replace back

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    file = BeautifulSoup(html, "html.parser")
    #now soup has the parsed html download
    tags = file("a") #stores all the tags in tag gets the anchor tag
    for tag in tags:
       ref = tag.get("href", None) #gets the contents of the links
       position = position - 1 #decreases counter
       if position == 0:
           break #breaks out of loop

    count = count - 1 #decreases counter
    position = keepposition #resets position back
    url = ref
print(tag.contents[0])
