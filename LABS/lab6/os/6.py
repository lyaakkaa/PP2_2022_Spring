import os

d = os.mkdir('folder to f.py')
path = 'folder to f.py'


for i in range(26):
    name = f'{chr(ord("A") + i)}.txt'
    file = os.path.join(path, name)
    files = open(file, 'w').close