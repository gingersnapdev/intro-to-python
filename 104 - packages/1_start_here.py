# you've imported one file from a folder now
# i bet you feel so fucking smart
# you might have noticed
# we've officially left w3schools' tutorial on python
# everything from here on out is straight off the fucking dome baby

# anyways, shitposting aside, let's talk about packages
# packages are a collection of modules that are typically bundled together
# all files within a package are kinda pieced together cause they're all pieces that lead to a common end goal
# as you grow as a developer, you'll familiarize yourself with all sorts of different packages
# but youre not there yet, if youre reading this git repo it means you dont know shit
# and thats fine, you want to learn and that makes up for you not knowing anything - cause youre trying to fix that

# let's start by importing the "ENTIRE" pkg folder
from pkg import *

# now let's open up the pkg folder and take a quick look inside
# you'll see 5 files: __init__, child, parent, fun, and fruit
# open the __init__.py file, come back here when you're instructed to

# welcome back
# let's do some basic module stuff to test if this worked

person = parent.Parent("Ethyl Rosenberg", 57)
person.greeting()

fun.fun("Vi Gia Le")

# those all work normally
# but when we try to use stuff within fruit, it'll break since it wasn't included in the __all__ list
# fruit.myFavoriteFruit("apple") <-- this wont run and will throw an error