import json
import datetime

created_time = datetime.datetime.now()


def load_file():
    try:
        filename = 'apikeys.json'
        data = json.load(open(filename))
        return data
    except IOError:
        print('File not found!')


def save_file(data):
    try: 
        filename = 'apikeys.json'
        with open(filename, 'w') as jsonfeed:
            json.dump(data, jsonfeed)
    except IOError:
        print('File not found!')