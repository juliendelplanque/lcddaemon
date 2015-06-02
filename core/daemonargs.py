# -*- coding: utf-8 -*-
""" Command arguments parser for the lcddaemon.

    This uses the argparse module from the Python library.
"""

import json
from argparse import ArgumentParser


def read_json_file(json_filename="core/args-en.conf"):
    result = {}
    with open(json_filename, "r") as json_file:
        str_json = json_file.read()

        result = json.loads(str_json)

    return result


def parse_arguments():
    args_conf = read_json_file()

    parser = ArgumentParser(**args_conf[0])

    for i in range(1, len(args_conf)):
        # Manuel gesture of special elements
        arg_names = args_conf[i].pop('names')
        arg_type = args_conf[i].pop('type')

        if len(arg_names) == 1:
            parser.add_argument(arg_names[0], type=eval(arg_type),
                                **args_conf[i])
        elif len(arg_names) == 2:
            parser.add_argument(arg_names[0], arg_names[1],
                                type=eval(arg_type), **args_conf[i])
        else:
            raise TypeError("Config parser can not hold more than 2 names.")

    parsed = parser.parse_args()
    config = vars(parsed)

    # If user specify customized configuration file, then update config values
    user_file = config.pop("conf")
    if user_file:
        user_defined = read_json_file(user_file)
        config.update(user_defined)

    return config
