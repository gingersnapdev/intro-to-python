# this file is simple, just has 2 constructors
# a constructor for a Parent object
# then a constructor for a Child object
# lastly, a function called fun
# you can go back to the other file now

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, favoritecolor):
        super().__init__(name, age)
        self.favoritecolor = favoritecolor
        # only children care about their favorite color i guess

    def myfavoritecolor(self):
        print(f"My favorite color is {self.favoritecolor}!")

def fun(name):
    print(f'My name is {name}!')