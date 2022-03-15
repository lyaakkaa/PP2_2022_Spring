import os

path = input()
exists = os.access(path, os.F_OK)
read = os.access(path, os.R_OK)
write = os.access(path, os.W_OK)
execute = os.access(path, os.X_OK)

print(f'Existence: {exists}\nReadability: {read}\nWritability: {write}\nExecutability: {execute}')