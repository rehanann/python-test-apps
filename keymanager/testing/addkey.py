import argparse
import sys
import json
import datetime


# import local modules

import filehandler

# global vars
created_time = datetime.datetime.now()


def addkey(args):
    
    in_keys = filehandler.load_file()
    #in_keys = load_keys['nodes']
    # print(in_keys)
    # if type(in_keys) is dict:
    #     in_keys = [in_keys]

    appname = args.appname
    domainname = args.domainname
    ipaddr = args.ipaddr
    keyset = args.keyset
    user = args.user
    now_time = str(created_time)


    keys = []
    for item in range(keyset):
        # mydict = {}
        title = input("please enter key name: ")
        value = input("please enter password: ")
        keys.append({
            "mykey" : title,
            "myvalue" : value,
            "created_time" : now_time,
            "modified_time" : now_time
        })
    
    
    
    # my_data = in_keys["nodes"]
    my_nodes = {}
    my_nodes["appname"] = appname
    my_nodes["domainname"] = domainname
    my_nodes["ipaddr"] = ipaddr
    my_nodes["user"] = [user]
    my_nodes["keys_bundle"] = [keys]
    in_keys["nodes"].append(my_nodes)
    # print(in_keys)


    # in_keys["nodes"].append({
    #     "app_name" : appname,
    #     "domain_name" : domainname,
    #     "ippaddress" : ipaddr,
    #         "user" : [
    #             {
    #                 "username" : "name2",
    #                 "password" : "true"
    #             },
    #             {
    #                 "username" : "name2",
    #                 "password" : "true"
    #             }
    #         ],
    #         "keys_bundle" : [
    #             {
    #                 "key_name" : title,
    #                 "key_value" : value,
    #                 "cr_time" : now_time,
    #                 "mod_time" : now_time
    #             }
    #         ],
    #         "created_time" : now_time
    # })

    return filehandler.save_file(in_keys)