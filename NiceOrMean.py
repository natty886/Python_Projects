#
# Python:  3.6.4
#
# Author: Daniel A. Christie
#
# Purpose: Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producting a functional game.
#
#           NOTE, function_name(variable _means we pass in the variable.
#           return variable _means returning variable back to call function.


def start(nice=0,mean=0,name=""):
    # get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

    
def describe_game(name):
    """
        Check if new game or not
        If new, get user name
        If not, thank player for
        playing again and continue 
    """
    # meaning, if no user name,
    # it's a new user, we need their name
    if name != "":
        print("\nThank you for playing again. {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                   print("\nWelcome, {}!".format(name))
                   print("\nIn this game, you'll be greeted \nby several different people. \nChoose to be nice or mean")
                   print("but at the end of the game your fate \nwill be sealed by your actions.")
                   stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you to \converse. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("n\The stranger glares at you \nmenacingly and storms off...")
            mean = (mean +1)
            stop = False
        score(nice,mean,name) # pass 3 variables to the score()


def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function passes values stored within 3 variables
    if nice > 2: # if valid, call win function passes to variables
        win(nice,mean,name)
    if mean > 2: # if valid, call lose
        lose(nice,mean,name)
    else:  # else call nice_mean function
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # sub {} wildcards with variable values
    print("\nNice job {}, you win! \nEveryone loves you!".format(name))
    # call again function and pass to variables
    again(nice,mean,name)

def lose(nice,mean,name):
    # sub {} wildcards with variable values
    print("\nGame Over! \n{}, you live wretched and alone!".format(name))
    # call again function and pass to variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nWanna play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Note, don't reset name variable since same user is playing again
    start(nice,mean,name)


    

if __name__ == "__main__":
    start()
