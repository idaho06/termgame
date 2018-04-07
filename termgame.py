#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
# import curses

from res.debug import Debug
from scenes import scenesdict, firstscene


def main(args):
    debug = Debug(args.debug)
    debug.out("No args except debug.")

    currentscene = scenesdict[firstscene]
    nextscene = currentscene.run()
    while nextscene != 'scene.end':
        currentscene = scenesdict[nextscene]
        nextscene = currentscene.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("-d", "--debug", help="Print debug info.", action="store_true")
    args = parser.parse_args()
    main(args)
