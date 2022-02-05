import re #imports regular expression python library
file = input("Enter a file")

if(len(file) < 1):
    file = "actualdata.txt"

filehndlr = open(file,"r") #opens file on read mode
total = 0
for line in filehndlr:
    line = line.rstrip()
    y = re.findall("[0-9]+",line)
    if len(y) > 0:
        for x in y:
            total += int(x)
print(total)