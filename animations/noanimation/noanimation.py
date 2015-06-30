#-*- coding: utf-8 -*-
""" This script contains an animation class that does no animation.
    It just display the contents of the message on the lcd without overhead
    management or anything.

    This class is used as the default animation.
"""

import time

from animations.abstractanimation import AbstractAnimation

class OneLineNoAnimation(AbstractAnimation):
    def animate(self, message):
        """ Just take the message contents and display it on the lcd screen on
            one line.

            Nothing is done for line overhead.
        """
        self.driver.clear()
        self.driver.write_lines((message.contents,))
        time.sleep(message.duration)

class MultiLineNoAnimation(AbstractAnimation):
    def animate(self, message):
        """ Split the message contents using '\n' character and display
            n first lines on the lcd screen (according to the linecount()
            method of the driver used).

            Nothing is done for line overhead.
        """
        strings = message.contents.split('\n')[0:self.driver.line_count()]
        self.driver.clear()
        self.driver.write_lines(strings)
        time.sleep(message.duration)
