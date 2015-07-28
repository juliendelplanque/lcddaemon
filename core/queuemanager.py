#-*- coding: utf-8 -*-
""" This script contains the object that has the responsability to pop messages
    from the queue, apply a specific method with the module loaded and then to
    pass the message to the object responsable of the animation.
"""

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
            except Exception as e:
                print("An exception occurs while managing the message: "+str(message))
                print("Here are some details:")
                print("Exception type: "+str(type(e)))
                print(str(e))

    def stop(self):
        """ Stop the loop that pop messages at next iteration.
        """
        self.keep_going = False
