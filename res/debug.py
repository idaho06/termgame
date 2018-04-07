#!/usr/bin/env python3
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Debug:
    def __init__(self, debug=False):
        self.debug = debug

    def out(self, tag="", message=""):
        if self.debug:
            eprint("DEBUG: TAG: {}".format(tag))
            eprint(message)
        else:
            pass

    def error(self, tag="", message=""):
        if self.debug:
            eprint("ERROR: TAG: {}".format(tag))
            eprint(message)
        else:
            pass