# recursion in this sense really means when a function calls itself
# consider the following:

def recursion():
    print("hello")
    recursion()

recursion()

# this yields the following:
# an error message: maximum recursion depth exceeded while calling a Python object
# hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello 
# the first thing basically means that there's a limit to how many times a recursive function can call itself
# and you hit the limit

# why use recursion over a loop?
# 