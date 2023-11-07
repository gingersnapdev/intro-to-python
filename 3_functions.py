# declare a function with def
def function():
    print("Hello")

# python doesnt care about void or anything like that
# you dont have to declare a return type, just return something
def noreturntype():
    x = "It never mattered"
    return x

# passing in variables is the same, sorta
# you dont need to declare what the variable type is
def dontdeclarevariabletypes(x):
    print("Hello")

# i mean you can if you want but it's not necessary
# but it does help when you're writing code that's going to be reviewed by others
# so people know what's supposed to be passed in
# this is called function annotation, well, the first part of function annotation anyways
def declare_variable_types(x:int, y:str):
    print("Hello")

# you can also imply the type of data that's being returned
# this is the 2nd part of function annotation
def implication(x:int) -> int:
    return 1

# python is funny cause even if you declare the type of data thats being returned
# if you dont return the specified type it doesnt break
def lmao(x:int) -> str:
    return 5

# whats even funnier is that if in your function, you declare the type of variable that comes in
# and you pass in the incorrect variable type
# it still doesnt break your code still runs
# the below function call will print 5, because the lmao function returns 5 (an integer)
print(lmao("weenie"))

# why doesn't it break?
# because the creator of python believes that
# if you know how to do function annotation, you can write a fucking function that behaves the way it should
# its your fault if you fuck it up
# im not joking