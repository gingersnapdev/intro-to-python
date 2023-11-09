class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.name}, and I am {self.age} years old.")