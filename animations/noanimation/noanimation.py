#-*- coding: utf-8 -*-
""" This script contains an animation class that does no animation.
    It just display the contents of the message on the lcd without overhead
    management or anything.

    This class is used as the default animation.
"""

import time

from animations.abstractanimation import AbstractAnimation

class NoAnimation(AbstractAnimation):
    def animate(self, message):
        self.driver.clear()
        self.driver.write_lines((message.contents,))
        time.sleep(message.duration)
