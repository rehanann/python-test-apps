import argparse
import sys

parser = argparse.ArgumentParser()


parser.add_argument('init', type=str,
                    help='select the option')

# parser.add_argument('-t', '--title', type=str,
#                         help='title of the your key')
# parser.subparsers.add_argument('-v', '--value', type=str,
#                         help='value of the your key')

args = parser.parse_args()
# subargs = subparsers.parse_args()

if args.init:
    print('help')