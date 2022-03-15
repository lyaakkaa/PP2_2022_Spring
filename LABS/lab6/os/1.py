
import os
path = input()
l = os.listdir(path)
print(f'directories and files {l}')
print(f'Directories: {[i for i in l if os.path.isdir(os.path.join(path, i))]}')
print(f'Files: {[i for i in l if not os.path.isdir(os.path.join(path, i))]}')

