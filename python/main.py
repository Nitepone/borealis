import argparse
import logging
import sys

from borealis.follower import SimpleStripFollower
from borealis.leader import Leader

logging.basicConfig(level=logging.INFO)

# sub-command functions
def foo(args):
    print(args.x * args.y)

def follower(args):
    f = SimpleStripFollower(args.length)

    l = Leader()
    l.register(f)
    l.spin()

def mono(args):
    f = SimpleStripFollower(args.length)

    l = Leader()
    l.register(f)
    l.spin()

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('follower')
parser_bar.add_argument('--length', default=60)
parser_bar.set_defaults(func=follower)

# create the parser for the "mono" command
parser_bar = subparsers.add_parser('mono')
parser_bar.add_argument('--length', default=60)
parser_bar.set_defaults(func=mono)

# parse the args and call whatever function was selected
args = parser.parse_args(sys.argv[1:])
args.func(args)
