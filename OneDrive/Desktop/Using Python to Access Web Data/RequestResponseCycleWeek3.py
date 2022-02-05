import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a socket
#Here a socket instance is created and AF_INET refers to local family address ipv4, Sock_Stream refers means connection oriented TCP protocol
#More info : You can find the ip using python if connecting with TCP fails

mysock.connect(("data.pr4e.org",80)) #connects to host, port # of the web server
#now After connecting to the web server you have to send a GET request

cmd = ("GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()) #\r\n signifies EOL so \r\n\r\n is an empty line basically
#Encode converts strings into bytes and then bytes back into strings
#Second parameter is the web page that we are requesting
#Third parameter is the Protocol we are using to do it

mysock.send(cmd) #sending it

while True:
    data = mysock.recv(512) #gets the first 512 characters at at time from the webserver
    if len(data) < 1: #if empty file then breaks and closes the socket
        break
    print(data.decode(),end="") #prints the decoded data that goes from UTF back to to Unicode

mysock.close() #closes the socket