# welcome to the init.py file (im not typing the underscores)
# btw when you see stuff in python thats encased by 2 underscores (__init__, __main__ etc) those are called dunders
# dunder init dunder main etc
# so this is the __init__ file

# an __init__.py file is used to let your computer (your compiler really) know "hey this folder is a python package"

# it's very important that your packages have an __init__.py file in it (it wont work normally if you dont include it)
# the __init__.py file controls what gets imported when you type in from __ import *
# you control what gets imported when that statement is run with this __all__ list
__all__ = [
    "parent",
    "child",
    "fun",
]
# yes you have to put all in dunders
# notice how the items in this list are the names of the other files in this pkg folder
# that's uhh... that's what's being imported when you write from __ import *

# when writing your own packages, there are times when you don't want from __ import * to import everything-everything
# you leave those out of the __all__ list
# notice how "fruit" isn't in there, it's intentionally left out for a later part of the 1_start_here file
# oh yeah you can go back to 1_start_here now