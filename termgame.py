#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
from scenes import scenesdict, firstscene


def main():
    logging.debug("Entering Main function.")

    currentscene = scenesdict[firstscene]
    nextscene = currentscene.run()
    while nextscene != 'scene.end':
        currentscene = scenesdict[nextscene]
        nextscene = currentscene.run()

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Small terminal interactive program.",
                                     epilog="Made by César (Idaho06) Rodríguez Moreno.")
    # parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("-d", "--debug", help="Debug level: DEBUG, INFO, WARNING, ERROR or CRITICAL", default="WARNING")
    parser.add_argument("-o", "--erroroutput", help="File of error output. Default is stderr.", default="stderr")
    args = parser.parse_args()

    loglevel = logging.WARNING
    logoutput = None

    if args.debug == "DEBUG":
        loglevel = logging.DEBUG
    if args.debug == "INFO":
        loglevel = logging.INFO
    if args.debug == "ERROR":
        loglevel = logging.ERROR
    if args.debug == "CRITICAL":
        loglevel = logging.CRITICAL

    if args.erroroutput != "stderr":
        logoutput = args.erroroutput

    logging.basicConfig(level=loglevel, filename=logoutput,
                        format="%(asctime)s %(levelname)s: %(funcName)s: %(message)s")

    logging.info("Debug set to %s." % loglevel)

    exit(main())
