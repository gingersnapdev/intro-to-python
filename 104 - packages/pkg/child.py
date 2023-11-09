import parent

class Child(parent.Parent):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def favoritecolor(self):
        print(f"My favorite color is {self.color}!")