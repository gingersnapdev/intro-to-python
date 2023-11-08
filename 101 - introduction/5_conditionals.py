# if statements are easy:
fruit = "banana"
if fruit == "banana":
    print(f'your fruit is: {fruit}')

# you add an else in there in the situation your if statement is false
fruit2 = "apple"
if fruit2 == "banana":
    print(f'your fruit is banana')
else:
    print(f'your fruit is not banana, it is: {fruit2}')

# python has else if, elif
# else if = also test this condition in the event that your first if statement isnt true
fruit3 = "kiwi"
if fruit3 == "banana":
    print('your fruit is banana')
elif fruit3 == 'kiwi':
    print('your fruit is kiwi')
else:
    print(f'your fruit is not kiwi or banana, it is: {fruit3}')

# the equal sign is also important
# 1 equal sign - setting something to something
# x = 4, we set x's value to 4
# 2 equal sign - we make a comparison
# x == 4 - we check if x is equal to 4
# x == 4 can result in a boolean (True or False)
a = 4
b = 5
if b == a:
    print('b is equal to a')
else:
    print('b is not equal to a')

# if youre saucy you can shorthand your if statements
if a < b: print('a is less than b')

# if youre super saucy you can shorthand your if else statements too
# this is called a ternary operation
# or a conditional expression
# only nerds use those terms
print('saucy a is greater than b') if a > b else print('saucy a is less than b')

# then you have some keywords you can throw in for more complex comparison
# and - both conditions must match
if a < b and a!=b:
    print("and statement")
# or - one of these statements must match
if a > b or a < b:
    print('or statement')
# not - negates the condition
if not a > b:
    print('not statement')

# if statements cannot be empty
# but if for whatever reason you want them to be empty
# put a pass statement in there
if a < b:
    pass