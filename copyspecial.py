#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Bethany Folino with help from Jacob Short"

import re
import os
# from datetime import datetime
# from os import listdir
import sys
import shutil
# import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    string_pattern = re.compile(r"(\w+?\_\_\w+\_\_\.\w+)")
    result = ""

    for file in os.listdir(dirname):
        result += os.path.abspath(file)

    matches = string_pattern.findall(result)
    final = [os.path.abspath(match) for match in matches]
    return final


def copy_to(path_list, dest_dir):
    """Given a path_list and dest_dir, copies files in path_list to dest_dir"""
    shutil.copyfile(path_list, dest_dir)


def zip_to(path_list, dest_zip):
    """Given a path_list, zips path_list files up into the given zip path"""
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--fromdir', help='dest dir special files come from')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if ns:
        copy_to(ns)
    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
