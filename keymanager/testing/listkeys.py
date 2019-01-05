import argparse
import json

# import local modules

import filehandler


def lists(args):
    li = args.list
    
    if li == "ALL":
        print('ALL')
    elif li == "LIST":
        print('Not ALL')
    