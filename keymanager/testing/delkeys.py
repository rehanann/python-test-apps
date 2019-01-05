import argparse
import json

# import local modules

import filehandler

def delkeys(args):
    in_keys = filehandler.load_file()

    delete = args.delete

    for myitem in in_keys["nodes"]:
        for k,v in myitem.items():
            if v == delete:
                print(f"{v}")