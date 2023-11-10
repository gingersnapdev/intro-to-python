# now we're on data structures
# welcome to hell
# i might use both list and array in this doc since it's gonna be a long one
# for all intents and purposes, theyre the same in this scenario
# i learned how to do all this in java leave me alone

# here's our list
testlist = [1, 2, 3, 4, 5]

# 1.
# append(value):
# add something to the end of the list
testlist.append(7)
# [1, 2, 3, 4, 5, 7]

# 2.
# insert(position, value):
# insert something in a certain position in the list
# remember - computers start counting at 0
testlist.insert(5, 6)
# [1, 2, 3, 4, 5, 6, 7]

# 3.
# remove(value)
# remove an item from the list based on the value provided
# it only removes the first instance that the value appears in
removelist = [1, 2, 3, 3, 4, 5]
removelist.remove(3)
# [1, 2, 3, 4, 5]

# 4. 
# pop(position)
# remove the item at the given position at the list and return it
# if no position is specified, pop() removes the last item in the list
testlist.pop()
# 7
removelist.pop()
# 5

# 5.
# clear()
# remove all items in the list
removelist.clear()
# []

# 6.
# index(value, start, end)
# conducts a search within the list for the given value
# start and end dictate 2 positions in the list where the search -
# will start and end
indexlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 7

# 7.
# count(value)
# returns the number of times value appears in the list
countlist = [1, 2, 3, 4, 5, 5, 5]
countlist.count(5)
# 3

# 8.
# sorted(list, key, reverse)
# sorts your list
# takes 3 arguments
# 1 - the iterable to sort
# 2 - something used to compare each element in the sorted list to
# 3 - reverse, is this list sorted in asc(False) or desc(True)
sortlist = [6, 3, 8, 12, 5, 9, 4]
print(sorted(sortlist, reverse=False))

# 9.
# reverse()
# reverses the list
reverselist = [1, 2, 3, 4, 5]
reverselist.reverse()
# [5, 4, 3, 2, 1]

# 10.
# copy()
# returns a copy of the list
copylist = [1, 2, 3, 4, 5]
print(copylist.copy())

# this also does the same thing
print(copylist[:])

# hi lol