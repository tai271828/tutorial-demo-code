#!/usr/bin/env python3
#
# all_variable.py
#
# Description:
# ------------
# 'from xxx import *' is not recommended in python code but
# frequently adapted in console mode when testing code.
#
# the variable __all__ is a convention to tell the import
# behavior to import and only import the classes and methods
# included in the __all__
#
# Usage:
# ------
# $ python3
# $ from all_variable import *
# and then observe which function and class is imported.
#

__all__ = ["fun_a",
           "fun_b",
           "Class_b"]

def fun_a():
    pass

def fun_b():
    pass

def fun_c():
    pass

class Class_a:
    pass

class Class_b:
    pass

class Class_c:
    pass
