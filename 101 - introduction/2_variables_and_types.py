# integer
a = 4
print(f"\nIntegers:\n", a, type(a))

# string
# there are no chars in python
# every char is a string thats 1 character
b = "bananas"
print(f"\nStrings:\n", b, type(b))
c = "c"
print(c, type(c))

# floats
# there are no doubles in python
# only floats
d = 4.5
print(f"\nFloats:\n", d, type(d))

# booleans
# either equal to True or False
# used to compare things
boo = 1>4
print(f'\nboo is: {boo}\n')
boo2 = 1<4
print(f'\nboo2 is: {boo2}\n')

# lists
# it's the same as an array
# these are mutable = you can change the values once you create it
# these are ordered
# you can iterate (list[1], list[2], etc) through a list
# you can have duplicate values in a list
# python just calls them lists
e = [1, 2, 3, 4, 5]
print(f"\nLists:\n", e, type(e))

# sets
# a type of array, has some cool built-in features
# these are mutable (you can change a set and its items once its created)
# these are unordered
# you cannot iterate (set[1], set[2], etc) to get an individual value
# you cannot have duplicate elements
f = {"Austin", "Sweeney", 27.4, 1996, False, "Austin"}
print(f"\nSets:\n", f, type(f))

# tuples
# another type of array with some of its own unique traits
# there are immutable (you cannot change a tuple or its items once its created)
# these are ordered
# you can iterate (tuple[1], tuple[2], tuple[3], etc) through a tuple
# you can have duplicate elements
g = ("Lotito", "Anthony", 27.5, 1997, True, "Anthony")
print(f"\nTuples:\n", g, type(g))


# dicts (DICTionary)
# this one is important most work-related stuff you do in python youre gonna use a dict
# dicts are basically just key value pairs (key: value)
# keys must be unique
# values can be duplicates
# can contain multiple data types
# you use these a lot when working with APIs
h = {
    "firstname": "Austin",
    "lastname": "Sweeney",
    "age": 27,
    "is_gay": True
}
print(f"\nDicts:\n", h, type(h))