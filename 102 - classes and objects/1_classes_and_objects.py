# a class is a constructor
# think of it as a blueprint for objects
# an object is created with parameters and statements provided by the class

class person:
    age = 26
    favorite_fruit = "apple"
    job = 'eastern european staff blockchain developer III'

# create an object by doing this
vi = person()

# in my pretend little world:
    # everybody is 26 years old
    # their favorite fruit is apples
    # and their job is being a suspicious ass blockchain dev in belarus

# now every person that's created using the "person" class will have:
    # the same job
    # the same age
    # the same favorite fruit

austin = person()
tony = person()

print(f"Tony's age is: {tony.age}")
print(f"Austin's favorite fruit is: {austin.favorite_fruit}")
print(f"Vi's job is: {vi.favorite_fruit}") # this is intentional its funny