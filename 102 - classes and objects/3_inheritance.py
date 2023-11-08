# i dont know how to spell inheritance so if its spelled wrong you can eat my ass
# also called parent class and child class by some developers and teachers
# in java it's called super

# let's say we have a class, let's go with person again
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old!")

# inheritance refers to the child class
# a subset of the parent class (you pass in a Parent when you create a Child object)
# this means that a child has all the traits (parameters and functions) of a parent (parent object)
class Child(Parent):
    pass

# imagine 2 random people i just made up
# Gladys Smith is a 45 year old woman
# Gladys has a son, Tim, who is 12 years old
gladys = Parent("Gladys Smith", "45")
tim = Child("Tim Smith", 12)

gladys.greeting()
tim.greeting()

# gladys has a 2nd child, chris
# chris decided he didnt wanna be like his parents and tim
# they didnt go to college so they could manage the family gas station
# chris thinks hes better than that
# chris gets his own __init__ function now so he's different from his mom and tim
# chris' name is now differentiated between first and last name
# and he gets to go to college
# now since chris gets his OWN init function he has different properties than his parents and tim
# cause chris wanted to go to fucking college

# __init__ functions in the child class override the __init__ function they inherit from the parent class
class Child2(Parent):
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college

chris = Child2("Chris Smith", 18, "UCLA")
# since we didnt override the greeting function he still inherits the greeting function
chris.greeting()

# we can also use the super function to inherit EVERYTHING from the parent
class Child3(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)

# if we wanna make chris super super unique from his family:
# we can also add new properties and functions as well
class Child4(Parent):
    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college
    
    def iwenttocollege(self):
        print(f"My name is {self.name} and I attended {self.college}, so I'm better than my family!")

chris2 = Child4("Chris Smith", 20, "UCLA")
chris2.greeting()
chris2.iwenttocollege()