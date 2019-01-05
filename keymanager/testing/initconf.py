import argparse
import json
import datetime

#import local modules

import filehandler
import addkey

# import local modules
created_time = datetime.datetime.now()

def initialize_conf(args):
    print('Configration initialized')
    global created_time
    now_time = str(created_time)

    project_name = args.project
    domin_name = args.domainname
    
    in_keys = {
      "project_name" : project_name,
      "initilize_time" : "duration of config data init",
      "created_time" : now_time,
      "parent_dom" : domin_name, 
      "nodes" : [
        ]
    }
    return filehandler.save_file(in_keys)
    