#-*- coding: utf-8 -*-
""" This script contains function to help loading a module.
"""

import imp
import sys

from modules.abstractmodule import AbstractModule

def load_module_from_conf(configuration):
    """ Try to load the module defined in the configuration if there is one.
        If this works, return the class that has to be used in MessageManager.

    Keyword Arguments:
        configuration - A dictionnary of configuration.
    """
    module_path = configuration["module_path"]
    module_classname = configuration["module_class"]
    try:
        module = imp.load_source('module', module_path)
        module_class = getattr(module, module_classname)
        if not issubclass(module_class, AbstractModule):
            print("Error: "+module_classname+" is not a subclass of"+\
                  " modules.abstractmodule.AbstractModule.")
            sys.exit(-1)
        else:
            return module_class
    except Exception as e:
        print("Error: an exception occurs while loading the module.")
        print("Here are details about it: \""+str(e)+"\"")
        sys.exit(-1)
