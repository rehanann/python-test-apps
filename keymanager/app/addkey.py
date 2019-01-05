import argparse
import sys
import json
import datetime


# import local modules

import filehandler

# global vars
created_time = datetime.datetime.now()


def addkey(args):
    
    apikeys = filehandler.load_file()
    
    if type(apikeys) is dict:
        apikeys = [apikeys]

    title = args.title
    value = args.value
    
    global created_time
    now_time = str(created_time)

    apikeys.append({
        "name" : title,
        "value" : value,
        "created_time" : now_time
    })

    return filehandler.save_file(apikeys)