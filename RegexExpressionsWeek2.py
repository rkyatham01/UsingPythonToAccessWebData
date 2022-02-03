#Using RegEx Expressions to read a file
#look for Integers
#and Use Re.findall() to look for numbers
#find the sum of them
import re

file = input("Enter a file name: ")

if (len(file) < 1):
    file = "ActualData.txt"

filehdnlr = open(file, "r") #Put on read mode
sum = 0 #where u put the sum of the numbers

for line in filehdnlr:
    line = line.rstrip()
    add = re.findall("[0-9]+",line) #finds the 0-9 ,
    #1 or more numbers and puts them in
    #Here add is a array of strings of numbers
    if len(add) > 0:
        for lines in add:
            sum += int(lines)
print(sum)