import json
import datetime

#import local modules

import filehandler
import addkey

# import local modules
created_time = datetime.datetime.now()

def initialize_conf():
    print('Configration initialized')
    global created_time
    now_time = str(created_time)
    # data = [
    #         {
    #         "name" : 'master',
    #         "value" : 'key',
    #         "created_time" : now_time
    #     }
    # ]
    in_keys = {
      "project_name" : "name",
      "initilize_time" : "duration of config data init",
      "created_time" : "date and time",
      "parent_dom" : "domain_name", 
      "nodes" : [
        ]
    }
    return filehandler.save_file(in_keys)
    