import json
import argparse
import sys

with open('tango.json', 'r') as jsonfeed:
        apikeys_dict = json.load(jsonfeed)

apikeys = json.dumps(apikeys_dict, indent=2)
Nlist = eval(apikeys)
# print(type(Nlist))
# print(Nlist)
# print(type(Nlist[1]))

# for list in Nlist:
#     for key,value in list.items():
#         # if value == "mykeys1":
#             print(key,value)

# for list in Nlist:
#     for key,value in list.items():
#         # if value['name'] == "mykeys1":
#             print(value)

# for list in Nlist:
#     print(list)
#     print(type(list))


# for list in Nlist:
#     print(list['name'])
#     print(list['value'])


for list in Nlist:
    if (list['name']) == 'mykeys1':
        print(list['value'])
# for list in Nlist:
#     for k,v in list.items():
#         print(f"this is 1 :{k} and this is value: {v}")

# for list in Nlist:
#     for k,v in list.items():
#         if (v['name']) == 'mykeys1':
#             print(v['value'])