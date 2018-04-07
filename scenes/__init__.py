import importlib
import os


class Scene:
    def __init__(self):
        pass

    def run(self):
        pass


sceneslist = ['scenes.presentation']
scenesdict = {}
firstscene = 'scenes.presentation'

for s in sceneslist:
    scenesdict[s] = importlib.import_module(s)
