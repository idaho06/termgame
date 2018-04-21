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

for scene in sceneslist:
    scenesdict[scene] = importlib.import_module(scene)
