import json
file = open('sample.json', 'r')
text = file.read()
d = dict()
d = json.loads(text)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")

for i in d['imdata']:
    print(f'{i["l1PhysIf"]["attributes"]["dn"]}       {i["l1PhysIf"]["attributes"]["descr"]}                       {i["l1PhysIf"]["attributes"]["speed"]}  {i["l1PhysIf"]["attributes"]["mtu"]}')