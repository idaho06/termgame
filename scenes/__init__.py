import importlib
import logging

class Scene:
    def __init__(self):
        pass

    def run(self):
        pass


logging.debug("Importing scenes.")

sceneslist = ['scenes.presentation', 'scenes.login']
scenesdict = {}
firstscene = 'scenes.login'

for scene in sceneslist:
    logging.debug("Importing scene: %s" % scene)
    scenesdict[scene] = importlib.import_module(scene)
