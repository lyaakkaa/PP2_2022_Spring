import os
file = open("example.txt","r")
cnt = 0
text = file.read()
CoList = text.split("\n")
for i in CoList:
    if i:
        cnt += 1      
print("Number of lines:", cnt)