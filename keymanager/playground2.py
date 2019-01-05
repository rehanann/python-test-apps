"""
Start with create Key value file from command line
"""
import json


def add_key(args):
    
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
    

def initilize_conf():
    pass

def list_key():
    pass

def del_key():
    pass


def get_user_choice():
    user_input = input('Select Your Choice: ' )
    return user_input

waiting_for_input = True
while waiting_for_input:
    print('Please Choose: ')
    print('1: Initlize Configuration: ')
    print('2: Add Key: ')
    print('3: List Keys: ')
    print('4: Delete Key: ')
    print('q: Quit: ')

    user_choice = get_user_choice()
    if user_choice == '1':
        initilize_conf()
    elif user_choice == '2':
        add_key()
    elif user_choice == '3':
        list_key()
    elif user_choice == '4':
        del_key()
    elif user_choice == 'q':
        break
