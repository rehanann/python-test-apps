
import argparse
import sys
import json
import datetime


# import local modules

import filehandler
import addkey
import initconf

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

parser.add_argument('-i', '--initialize_conf', type=str,
                        dest='initialize_conf', help='select the option')
parser.add_argument('-a', '--add_key', type=str,
                        dest='add_key', help='select the option')
parser.add_argument('-l', '--list_keys', type=str,
                        dest='list_keys', help='select the option')
parser.add_argument('-m', '--check_key', type=str,
                        dest='check_key', help='select the option')
parser.add_argument('-d', '--del_key', type=str,
                        dest='del_key', help='select the option')
parser.add_argument('-t', '--title', type=str,
                        help='title of the your key')
parser.add_argument('-v', '--value', type=str,
                        help='value of the your key')
args = parser.parse_args()


args = parser.parse_args()
if args.add_key:
    addkey.addkey(args)
elif args.initialize_conf:
    initconf.initialize_conf()
elif args.list_keys:
    print(list_keys())
elif args.check_key:
    check_key(args)
elif args.del_key:
    del_key(args)