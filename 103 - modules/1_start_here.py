# a module is a library of code that's reused throughout your project
# its a lot simpler to explain in a directory environment than on a webpage
# let's start off by taking a look at the modules folder, go ahead and open it, then open constructors.py

# so let's start off by importing that constructors.py file
from modules import constructors
# this looks a bit different
# it basically reads as:
# FROM the modules folder, IMPORT the constructors.py file

# we can access the stuff insice of the constructors.py file by prefixing your stuff with "constructors"
child = constructors.Child("Steve", 8, "Blue")
constructors.fun("Vi Le")

# when you use a module to create an object
# after the object is created, you dont need to add the constructors prefix to access some of the stuff within it
child.myfavoritecolor()
