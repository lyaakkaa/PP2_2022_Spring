import os

with open('lyaka.txt','r') as file1:
    with open('lyaka2.txt','a') as file2:
        for i in file1:
            file2.write(i)
    file2.close()