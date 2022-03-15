import os

path = input()
if os.path.exists(path):
    print(os.getcwd())
    if os.path.isdir(path):
        print(os.listdir(path))
    else:
        file = os.path.basename(path)
        print(file)
else:
    print("None")