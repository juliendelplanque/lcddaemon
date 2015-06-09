#-*- coding: utf-8 -*-

import time

from animations.abstractanimation import AbstractAnimation
from animations.noanimation.noanimation import MultiLineNoAnimation

class LeftToRightAnimation(AbstractAnimation):
    pass

class RightToLeftAnimation(AbstractAnimation):
    def __init__(self, driver):
        # Call super class constructor.
        super().__init__(driver)
        # Re-use an animation already created.
        self.multi_no_animation = MultiLineNoAnimation(driver)

    def animate(self, message):
        strings = message.contents.split('\n')
        max_string_size = max([ len(string) for string in strings ])
        if max_string_size > self.driver.line_size(): # Need to shift contents
            move_to_do = max_string_size - self.driver.line_size() + 1
            time_per_frame = message.duration/move_to_do
            for i in range(move_to_do):
                strings_to_display = [string[i:i+self.driver.line_size()]
                                        for string in strings]
                self.driver.clear()
                self.driver.write_lines(strings_to_display)
                time.sleep(time_per_frame)
        else: # No need to shift contents
            self.multi_no_animation.animate(message)
