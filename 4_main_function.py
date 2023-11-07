# declaring a main function in python is a bit different

def main():
    print("You're inside the main function!")

if __name__ == "__main__":
    main()

# why is it weird? what the fuck is __name__?

# consider the following:
# when you run a python file, it does everything in the program
# when you run a python file, the python interpretor (your IDE or terminal for the most part) assigns the module (the file itself) a name (__name__) (other than the regular name of the file)
# when YOU specifically run this file, the interpretor gives the module a name, "__main__", because it's the main file
# when you write bigger programs or scripts, and it requires the use of multiple python files, it's "name" (__name__) only the file you specifically run in your -
# - IDE or terminal will be called __main__
# if a python file is called and executed as part of a script (file a calls a function in file b), file b is not named __main__, it's named something else
# because python files execute everything when you run it, you need a way to control what's being run so you dont break your computer
# so that's why the main function is like that, the main function is used to control what happens in your file when you run the code
# you do not need a main function if your script or file is able to do what it needs to do by itself (in one file)
# you need a main function when your job requires the use of multiple python files (libraries excluded)