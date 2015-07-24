#-*- coding: utf-8 -*-
import time

from animations.abstractanimation import AbstractAnimation
from animations.noanimation.noanimation import MultiLineNoAnimation

class VerticalAnimation(AbstractAnimation):
    def __init__(self, driver):
        # Call super class constructor.
        super().__init__(driver)
        # Re-use an animation already created.
        self.multi_no_animation = MultiLineNoAnimation(driver)

    def animate(self, message):
        strings = message.contents.split('\n')
        if len(strings) > self.driver.line_count():
            self.display(message, strings)
        else:
            self.multi_no_animation.animate(message)

    def display(self, strings):
        raise NotImplementedError()

class TopToBottomAnimation(VerticalAnimation):
    def display(self, message, strings):
        time_per_frame = message.duration/len(strings)
        for i in range(len(strings)):
            strings_to_display = strings[i:i+self.driver.line_count()]
            self.driver.clear()
            self.driver.write_lines(strings_to_display)
            time.sleep(time_per_frame)

class BottomToTopAnimation(TopToBottomAnimation):
    def display(self, message, strings):
        strings.reverse()
        super().display(message, strings)
