import argparse
import sys
import json
import datetime


# import local modules

import filehandler
import addkey
import initconf
import listkeys
import delkeys

# global vars
created_time = datetime.datetime.now()

def check_key(args):
    name = args.title
    # with open('tango.json', 'r') as jsonfeed:
    #     apikeys_dict = json.load(jsonfeed)
    apikeys_dict = filehandler.load_file()
    
    apikeys = json.dumps(apikeys_dict, indent=2)
    # print(type(apikeys))
    Nlist = eval(apikeys)
    # print(type(Nlist))
    # print(Nlist[1])
    # print(type(Nlist[1]))
    for list in Nlist:
        if (list['name']) == name:
            #return list['value']
            print(f"Key : {list['name']}, value: {list['value']}")
       
def list_keys():
    with open('tango.json', 'r') as jsonfeed:
        apikeys_dict = json.load(jsonfeed)
    
    apikeys = json.dumps(apikeys_dict)
    apikeys = eval(apikeys)
    #return apikeys
    print(apikeys)

    
def del_key(args):
    name = args.title
    with open('tango.json', 'r') as jsonfeed:
        apikeys_dict = json.load(jsonfeed)
    
    apikeys = json.dumps(apikeys_dict, indent=2)
    # print(type(apikeys))
    Nlist = eval(apikeys)
    # print(type(Nlist))
    # print(Nlist[1])
    # print(type(Nlist[1]))
    for list in Nlist:
        if (list['name']) == name:
            # print(f"Key : {list['name']}, value: {list['value']}") 
            del list['name']
            del list['value']
            print(list)
            #print(f"Key : {list['name']}, value: {list['value']} is deleted")
            apikeys = json.dumps(list)
            print(apikeys)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


# Init module

parser_init = subparsers.add_parser('init')
parser_init.add_argument('-p', '--project')
parser_init.add_argument('-d', '--domainname', default='None')
parser_init.set_defaults(func=initconf.initialize_conf)


# addkeys module

parser_addkey = subparsers.add_parser('add')
parser_addkey.add_argument('-a', '--appname')
parser_addkey.add_argument('-d', '--domainname', default='None')
parser_addkey.add_argument('-ip', '--ipaddr', default='None')
# parser_addkey.add_argument('-t', '--title')
# parser_addkey.add_argument('-v', '--value')
parser_addkey.add_argument('-u', '--user', action='append')
parser_addkey.add_argument('-k', '--keyset', type=int)
parser_addkey.set_defaults(func=addkey.addkey)

# remove
parser_del = subparsers.add_parser('delete')
parser_del.add_argument('-d', '--delete')
parser_del.add_argument('-a', '--all')
parser_del.set_defaults(func=delkeys.delkeys)



# list
parser_list = subparsers.add_parser('list')
parser_list.add_argument('-l', '--list')
parser_list.add_argument('-a', '--all')
parser_list.set_defaults(func=listkeys.lists)

# update


args = parser.parse_args()
args.func(args)
