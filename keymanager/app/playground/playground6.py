import json
import os

def load_file():
    filename = 'apikeys.json'
    data = json.load(open(filename))
    return data


def save_file(data):
    try: 
        #global apikeys
        filename = 'apikeys.json'
        with open(filename, 'w') as jsonfeed:
            json.dump(data, jsonfeed)
    except IOError:
        print('File not found!')

def addkey():
    
    apikeys = [
            {
            "name" : 'master',
            "value" : 'key',
            "created_time" : 'now_time'
        }
    ]
    return save_file(apikeys)

addkey()

def addnewkey():
    #data = json.load(open('apikeys.json'))
    data = load_file()
    # print(type(data))
    # print(data[0])
    if type(data) is dict:
        #print('list')
        data = [data]
    data.append(
        {
            "name" : 'newkey',
            "value" : 'key',
            "created_time" : 'now_time'
            }
        )
        
    return save_file(data)

addnewkey()