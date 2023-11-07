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

# lists
# it's the same as an array
# these are mutable = you can change the values once you create it
# python just calls them lists
e = [1, 2, 3, 4, 5]
print(f"\nLists:\n", e, type(e))

# sets
# i have no idea what a set is
# these are immutable = you cannot change it once its created
# things in a set can be different data types
# not ordered, cannot be accessed by its positional index
# does not allow duplicate values
# notice how Austin appears twice when i declare the set, but only appears once when i print the set
f = {"Austin", "Sweeney", 27.4, 1996, False, "Austin"}
print(f"\nSets:\n", f, type(f))

# tuples
# i also have no idea what this is
# these are mutable = you can change the values once you create it
# these are ordered
# allow duplicate values
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