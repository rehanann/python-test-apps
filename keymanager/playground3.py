import argparse
import sys
import json

# def main():
#     parser = argparse.ArgumentParser()

#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', '--initialize_conf', type=str,
#                             dest='initialize_conf', help='select the option')
#     parser.add_argument('-a', '--add_key', type=str,
#                             dest='add_key', help='select the option')
#     parser.add_argument('-t', '--title', type=str,
#                             help='title of the your key')
#     parser.add_argument('-v', '--value', type=str,
#                             help='value of the your key')
#     args = parser.parse_args()

#     print('initlize_conf    =  {!r}'.format(args.initialize_conf))
#     print('add_key    =        {!r}'.format(args.add_key))
#     print('title    =        {!r}'.format(args.title))
#     print('value    =        {!r}'.format(args.value))
    
    # user_choice = True
    # if user_choice == '-a':
    #     #sys.stdout.write(str(addkey(args)))

    # elif user_choice == '-i':
    #     initialize_conf()

def addkey(args):
    
    apikeys = json.load(open('tango.json'))

    if type(apikeys) is dict:
        apikeys = [apikeys]

    title = args.title
    value = args.value
    
    apikeys.append({
        "name" : title,
        "value" : value
    })
    #print(apikeys)
    
    with open('tango.json', 'w') as jsonfeed:
        json.dump(apikeys, jsonfeed)


def initialize_conf():
    print('Configration initialized')
    apikeys = [
            {
            "name" : 'null',
            "value" : 'null'
            }
        ]
    
    with open('tango.json', 'w') as jsonfeed:
        json.dump(apikeys, jsonfeed)



def list_keys():
    with open('tango.json', 'r') as jsonfeed:
        apikeys_dict = json.load(jsonfeed)
    
    apikeys = json.dumps(apikeys_dict)
    #return apikeys
    print(apikeys)


def check_key(args):
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
            #return list['value']
            print(f"Key : {list['name']}, value: {list['value']}")
       

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

if args.add_key:
    addkey(args)
elif args.initialize_conf:
    initialize_conf()
elif args.list_keys:
    print(list_keys())
elif args.check_key:
    check_key(args)
elif args.del_key:
    del_key(args)


# if __name__ == '__main__':
#     main()
