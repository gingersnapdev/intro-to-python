# while loops - execute as long as the given expression is true
x = 0
while x < 10:
    print(f'value for x: {x}')
    x+=1

# you can add an else statement after your loop
# the code in the else block executes when the loop is finished
y = 0
while y < 10:
    print(f'value for y: {y}')
    y+=1
else:
    print('the y loop has concluded')

# for loops are also simple
z = 5
for i in range(0, z):
    print(f'value for z: {i}')

# you can iterate through a data structure pretty easily

# let's start with a tuple
tup = ("i", "hate", "my", "job")
for i in tup:
    print(i)

# now let's do dicts
dic = {
    'item1': 'this is item 1',
    'item2': 'this is item 2',
    'item3': 'this is item 3'
}
for i in dic:
    # this prints the key
    print(i)
    # this prints the value
    print(dic[i])

# you can use the else block in for loops as well
for i in dic:
    print(dic[i])
else:
    print('end of dic')

# continue
# the continue keyword skips over that iteration of the loop when its hit
# you can control this with conditional statements
for i in dic:
    # if you hit the key 'item1', skip it
    if i == 'item1':
        continue
    print(i)

# break 
# ends the loop
word = "random"
for i in word:
    # prints all the letters in the word "random"
    # when it hits letter 'n', break out of the loop
    print(i)
    if i == 'n':
        break

# pass
# used for writing empty loops
for i in dic:
    pass
print(f'Last key in dictionary dic: {i}')

