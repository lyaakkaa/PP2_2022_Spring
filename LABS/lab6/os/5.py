l = input().split()
  
with open("example_2", 'a') as f: 
    for i in l:
        f.write(f'{i}\n')
    print("Success")
f.close()