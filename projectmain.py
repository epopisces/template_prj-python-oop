#! /usr/bin/python3

#? Using this template: delete all comments starting with '#?', they are helper text

__doc__ = """

Title - One line blurb

Paragraph describing the script or application

Usage:
    ./projectmain.py arg1 [optionalarg2]

Flags & Parameters
    -h, --help      
    param1          Thing 1 (required), expects a string of X chars
    param2          Thing 2 (optional)

Output:
    string_output   Thing 3.  6 chars starting with Thing

Examples:
    ./projectmain.py                    Will prompt for all arguments
    ./projectmain.py Thing1             Will prompt for 1 argument
    ./projectmain.py Thing1 Thing2      Will execute and return Thing 3
    ./projectmain.py -h                 Will output this help doc
    ./projectmain.py --help             Will output this help doc

"""
__author__ = "Firstname Lastname"
__date__ = "YYYY.MM.DD"
__version__ = 0.1

import logging, argparse    #? remove argparse if the script won't accept arguments
#? from tools.{toolname} import {toolname}_api as {toolname}

#? Optional imports that may be helpful
#?   toml (configuration file format for scripts)
#?   re (regex)
#?   os (get files or folders, or environment variables)

class PrimaryClass(object):
    """Oneline description (can have longer description below, if desired)
    
    Attributes:
        attr1 (str):        A required or optional attribute used in __init__
        attr2 (bool):       Another required or optional attribute used in __init__

    Methods:    
        method1()           One line explanation of method
        method2()           One line explanation of method
        method3()           One line explanation of method
    
    """
    
    def __init__(self):
        #? any stuff that needs to happen when this is initialized (like grabbing credentials,
        #? authentication, setting attributes equal to an initial value) happens here
        return

if __name__ == '__main__':
    # * Init logging

    # * Init argument handling.  Will automatically provide '-h, --help' functionality
    #? See https://docs.python.org/3/howto/argparse.html for more details
    parser = argparse.ArgumentParser(description="Write a brief description of the script here")
    parser.add_argument('-e','--examplearg', default=False, type=str, help='an example string arg')

    args = parser.parse_args() #? Any argument can be referenced by args.argname, eg 'args.examplearg'

    # * Init Class
    classexample = PrimaryClass()
    print(classexample.__doc__)
