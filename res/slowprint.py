#!/usr/bin/env python3

import sys, time, random


def type(t, typing_speed=50):
    for l in t:
        sys.stdout.buffer.write(bytes(l, 'utf-8'))
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print('')
    sys.stdout.flush()


def sigh(amount=1.0):
    time.sleep(amount + random.random() * 2.0)
