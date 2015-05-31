# -*- coding: utf-8 -*-
""" Command arguments parser for the lcddaemon.

    This uses the argparse module from the Python library.
"""

import json
from argparse import ArgumentParser


def get_args_parser_conf(args_conf_filename="core/args-en.conf"):
    args_conf = {}
    with open(args_conf_filename, "r") as args_conf_file:
        config_content = args_conf_file.read()

        args_conf = json.loads(config_content)

    return args_conf


def parse_arguments():
    args_conf = get_args_parser_conf()

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
    return vars(parsed)
