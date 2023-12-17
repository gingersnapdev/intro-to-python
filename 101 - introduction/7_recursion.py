# recursion in this sense really means when a function calls itself
# consider the following:

# def recursion():
#     print("hello")
#     recursion()
# recursion()

# this yields the following:
# an error message: maximum recursion depth exceeded while calling a Python object
# hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello 
# the first thing basically means that there's a limit to how many times a recursive function can call itself
# and you hit the limit

# for a less funny example that doesn't break your ide:

def fizzbuzz(x):
    if x != 0:
        if x%3==0 and x%5==0:
            print("fizzbuzz")
        elif x%3==0:
            print("fizz")
        elif x%5==0:
            print("buzz")
        else:
            print(x)
        x-=1
        fizzbuzz(x)
    else:
        print("x is 0!")

def main():
    x = 45 # this can be any number
    fizzbuzz(x)

if __name__ == "__main__":
    main()

# this is a question that gets asked on coding interview sometimes (if the bar is low anyways)
# if x is divisible by 3, print fizz
# if x is divisible by 5, print buzz
# if x is divisible by both, print fizzbuzz 


# why use recursion over a loop?
# sometimes you just need to
# loops really just iterate over stuff (a list, anything you can really count)
# recursion is somewhat easier to read and interpret (at least once you get to a certain point)
# when you're working with data structures, especially when you're working with large/unknown amounts of data
# you can't realistically iterate over that much stuff, it'll be difficult to keep count
# with recursion you can put a lot more control over your code, when it executes, when to not execute
    
# the fizzbuzz example above wasn't the best way to demonstrate the benefits of recursion over iterations (loops)
# but it was an easy way to show you how it works
# the benefits really show up when you work with data structures and algorithms
# so it's beneficial to keep recursion knowledge in your back pocket until this tutorial gets to that point