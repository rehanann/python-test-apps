"""
Main file for the application.
intend purpose to use for  declaring arguments and client commands options:-

options are:-
1. Initialize the configuration
appkey [-i, --init] init [-f, --filename] [-s, --strictlevel] [-h, --hash]=level of hashmap
appkey [-i, --init] init [-db, -dbase] [-s, --strictlevel] [-h, --hash]=level of hashmap
appkey.platform [-i, --init] init [-db, -dbase] [-s, --strictlevel] [-h, --hash]=level of hashmap

2. Add keys in to data
appkey -a --addkey --dbname=name -title=title --password=password --username=user --password=password

3. List keys from file or db
appkey -l listkeys --dbname=name

4. delete key
appkey -d keyname --dbname

5. list single key
appley -m viewkey --dbname



user can add key in dict or list form as below.
1. appkey -a addkey -l1 --dbname=name --title=key1 --pass=pass
2. appkey -a addkey -l2 --dbname=name --title=key1 --value=[{"value1": "key1"}, {"value2": "key2"}, {"value3": "key3"}]
3. appkey -a addkey -l2 --dbname=name --title=key1 --value=[{"value1": "key1"}, {"value2": "key2"}, {"value3": "key3"}] --appname=name
"""

"""
Data storege format:-
1. keyname
2. password
3. usernames
4. hostname
5. dbname
6. levels [l1, l2, l3]
7. date and time
8. if modify (new time)
9. level of strictness

'dateset' : {
    'keyname'      : 'keyname',
    'password'     : 'password',
    'username'     : 'username',
    'hostname'     : 'hostname',
    'strictlevel'  : 'l1',
    'dbname'       : 'dbname',
    'created_time' : 'datetime'
}

"""

import argparse
import sys
import json
import playground3
# Command Argument

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
    list_keys()
elif args.check_key:
    check_key(args)
elif args.del_key:
    del_key(args) 