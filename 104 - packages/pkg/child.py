# oh yeah you can import modules in the same directory by just importing the name of the file
from pkg import parent
# this looks weird, on your end it's supposed to just be
# import parent
# when i was writing this, my vscode loaded the entire directory (all the other folders and stuff)
# so my python imports may look a little wonky sometimes
# i just had to get this working so the code in the 1_start_here.py file would compile and run
# but usually for you it'd just be import parent

# which lets you do some wonky stuff (doesnt it look cool, separating your classes like this)
class Child(parent.Parent):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def favoritecolor(self):
        print(f"My favorite color is {self.color}!")