#-*- coding: utf-8 -*-
""" This script contains function to help loading a module.
"""

import imp
import sys

from modules.abstractmodule import AbstractModule
from drivers.abstractdriver import AbstractDriver
from animations.abstractanimation import AbstractAnimation

def load_from_conf(file_key, class_key, configuration, to_subclass, error_msg):
    """ Generic method that load a class from a python file using the
        configuration. This verify that the class loaded subclass to_subclass.
        If there is a problem, an error message is displayed and the program
        exit.

    Keyword Arguments:
        file_key      - The key to access the file path.
        class_key     - The key to access the class name.
        configuration - The configuration dict.
        to_subclass   - The class that must be subclassed.
        error_msg     - The error message to display in case there is a problem.
    """
    file_path = configuration[file_key]
    class_name = configuration[class_key]
    try:
        py_module = imp.load_source('pymodule', file_path)
        py_class = getattr(py_module, class_name)
        if not issubclass(py_class, to_subclass):
            print("Error: "+module_classname+" is not a subclass of "+\
                  str(to_subclass))
            sys.exit(-1)
        else:
            return py_class
    except Exception as e:
        print(error_msg)
        print("Here are details about it: \""+str(e)+"\"")
        sys.exit(-1)

def load_module_from_conf(configuration):
    """ Try to load the module defined in the configuration.
        If this works, return the class that has to be used in MessageManager.

    Keyword Arguments:
        configuration - A dictionnary of configuration.
    """
    return load_from_conf("module_path", "module_class", configuration, AbstractModule,
                          "Error: an exception occurs while loading the module.")

def load_driver_from_conf(configuration):
    """ Try to load the driver defined in the configuration.
        If it works, returns its class.

    Keyword Arguments:
        configuration - A dictionnary of configuration.
    """
    return load_from_conf("driver_path", "driver_class", configuration, AbstractDriver,
                          "Error: an exception occurs while loading the driver.")

def load_animation_from_conf(configuration):
    """ Try to load the animation defined in the configuration.
        If it works, returns its class.

    Keyword Arguments:
        configuration - A dictionnary of configuration.
    """
    return load_from_conf("animation_path", "animation_class", configuration,
                          AbstractAnimation,
                          "Error: an exception occurs while loading the driver.")
