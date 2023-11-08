# so in lesson 1 we went over classes
# we're going to go over the __init__ function now, which requires its own section
# it's a bit complex

# so usually when you create classes, you almost always utilize an __init__ function in it
# im gonna call the __init__ function "init" sometimes since i dont feel like typing it
# init basically means: run this when it's initialized
# in normal people words: if this is activated or initialized, do the following

# let's create a class with an init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# whoa what the fuck is all this what is "self"
# self means "itself", it's a way for a class/object to refer to itself
# if an object could talk like a person, self.name is an objects way of saying "My Name"
# when creating a new Person object, you dont have to pass in self, it's just there
# we're gonna try and make objects more dynamic (unique and changable)
# so when creating an object, we're passing in appropriate variables for this new init
# make sure theyre in order its gonna fucking break if its not

# oh yeah i forgot to mention when you do the below code youre creating an object
person1 = Person("Vi Gia Le", 26)
# we've created a new object, person1
# person1 name is Vi Gia Le (that's me) and his age is 26
print(f"Person 1's name is {person1.name} and he is {person1.age} years old.")

# -------------------
# the __str__() (im calling it str) function can be added to your class as well
# the str function is basically your class's return function
# when you invoke your class is represented as a string

class New_Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

person2 = New_Person("Vi Gia Le", 26)
print(person2)

# -------------------
# you can put functions in your class as well to get real saucy
# you can get pretty creative with these too
class New_New_Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def hello(self):
        print(f"Hello my name is {self.name}, it's great to meet you!")
    def imold(self):
        print(f"I'm {self.age} years old! I'm not getting any younger and the years are escaping me!")

person3 = New_New_Person("Vi Gia Le", 26)
person3.hello()
person3.imold()

# you can modify the properties of your objects
person3.age = 21
print(f"Yes Officer I am indeed {person3.age} I can legally buy alcohol fuck you")

# you can delete properties of your objects too
del person3.age
# this wont run it'll throw an error since person3 doesnt have an age
# print(person3.age)

# you can also delete your objects too
del person3

# you can use pass to create an empty class for whatever fucking reason
class Empty_Person:
    pass