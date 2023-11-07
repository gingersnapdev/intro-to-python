# how 2 print
print("How to print:")
print("Hello World")

# you can use either single quotes ' or double quotes "
# the differences are minute and youll barely utilize it
# oh wait when i was writing the example, it actually came up lmfao
# use double quotes when the string you're typing uses an apostrophe
print('Single Quote:')
print('This does not make a fucking difference')
print("Double Quote:")
print("Until your sentence uses an apostrophe, or something like that.")

# this will break so im gonna leave it in the comment as an example
# uncomment this line and see what happens
# print('this isn't gonna work')

# you can format your print statements with various escape characters
# start your print with an f, then your quotes, then insert whatever escape characters you want
# \n = new line
# go google the rest i dont know them i only really use \n
print(f"\nExample of some fun stuff you can do with\nEscape Characters\n")

# you can also put your raw variables in the middle of your string
# start your print with an f, then surround your variable name with {}
fruit = "banana"
print(f"I like eating {fruit}")