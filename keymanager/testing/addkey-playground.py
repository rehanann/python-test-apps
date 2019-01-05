
user = []
for item in range(5):
    item = input("enter username: ")
    user.append(item)

print(user)





# import json
# from collections import ChainMap

# l = 2

# # dic = [{
# #     "my_key" : "key1",
# #     "my_value" : "value1"
# # },{
# #     "my_key" : "key2",
# #     "my_value" : "value3"
# # }]

# item = int(input("enter your list range:"))
# print(item)

# data = []
# for item in range(item):
#     dic = {}
#     mykey = input("enter numbers of keys and ")
#     myvalue = input("enter your key name: ")
#     data.append({
#     "mykey" : mykey,
#     "myvalue" : myvalue
# })


# print(data)
# print(len(dic))

# print(type(dic))

# for k,v in dic.items():
#     print(f"{k} : {v}")

# data = []

# data.append(dic)
# print(data)

# in_keys = {"project_name": "myproject", "nodes" : [
#     ]
# }

# myjson = json.dumps(in_keys, indent=2)

# myjson2 = json.loads(myjson)
# # print(type(myjson2))
# # print(myjson2['nodes'])

# my2newjson = myjson2['nodes']
# # print(type(my2newjson))
# my2newjson.append(
#         {
#             "app_name" : "jenkins",
#             "user" : [
#                 {
#                     "username" : "name2",
#                     "password" : "true"
#                 },
#                 {
#                     "username" : "name2",
#                     "password" : "true"
#                 }
#             ],
#         }
#     )

# # print(my2newjson)

# my3newjson = myjson2['nodes']
# # print(type(my3newjson))
# my3newjson.append(
#         {
#             "app_name" : "vault",
#             "user" : [
#                 {
#                     "username" : "name2",
#                     "password" : "true"
#                 },
#                 {
#                     "username" : "name2",
#                     "password" : "true"
#                 }
#             ],
#         }
#     )

# # print(my3newjson)
# myjson4 = json.dumps(my3newjson, indent=4)
# print(myjson4)