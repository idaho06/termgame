#/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from debug import Debug
from slowprint import *

def main(args):
    debug = Debug(args.debug)
    debug.out("No args except debug.")
    type('¿No lo notas?.')
    sigh(3)
    type('Simplemente, algo no va bien, pero no sé muy bien qué ocurre.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("-d", "--debug", help="Print debug info.", action="store_true")
    args = parser.parse_args()
    main(args)