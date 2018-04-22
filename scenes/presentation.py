import logging
from res.slowprint import *
from scenes import Scene
from res import session


class Presentation(Scene):
    def run(self):
        type('Can you feel it?')
        sigh(2)
        type('Just, something is wrong, but I don\'t know what\'s going on.')
        sigh(1)
        print('\n' * 2)
        type('\nLemniscata.com presents', typing_speed=100)
        sigh(0.5)
        type('an AkinoSoft production:', typing_speed=100)
        sigh(0.5)
        type('\n\nThe Aberrant.', typing_speed=25)
        sigh(0.5)
        type('\n\n\n\n', typing_speed=15)
        sigh(1)

def run():
    logging.debug("Starting scene Presentation")
    presentation = Presentation()
    presentation.run()
    return 'scene.end'
