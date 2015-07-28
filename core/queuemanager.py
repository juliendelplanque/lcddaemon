#-*- coding: utf-8 -*-
""" This script contains the object that has the responsability to pop messages
    from the queue, apply a specific method with the module loaded and then to
    pass the message to the object responsable of the animation.
"""

import sys
import os

class QueueManager(object):
    """ Manage the MessageQueue.
    """
    def __init__(self, queue, module_class, animation):
        self.queue = queue
        self.module = module_class()
        self.animation = animation
        self.keep_going = True

    def manage(self):
        """ This method contains the loop that pop messages and manage them.
        """
        while self.keep_going:
            message = self.queue.pop()
            try:
                self.module.apply_actions_to(message)
                self.animation.animate(message)
                self.module.apply_post_actions_to(message)
            except Exception as e:
                print("An exception occurs while managing the message: "+str(message))
                print("Here are some details:")
                # Print informations about the exception.
                exc_type, exc_obj, exc_tb = sys.exc_info()
                file_name = exc_tb.tb_frame.f_code.co_filename
                print("- Exception type: "+e.__class__.__name__)
                print("- File name: "+file_name)
                print("- Line no: "+str(exc_tb.tb_lineno))

    def stop(self):
        """ Stop the loop that pop messages at next iteration.
        """
        self.keep_going = False
