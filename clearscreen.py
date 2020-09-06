from os import system
from time import sleep
from sys import stdout


def exitp(msg=" ", d=5):
    """Function to exit the program with a message"""
    print(f"\n{msg}\n")
    for i in range(d, 0, -1):
        print(f"Exiting Program in {i}", end='\r')
        stdout.write("\033[K")
        sleep(1)
    exit(1)


def clrscr(msg=" ", d=5):
    """Function to clear the screen with a message"""
    print(f"\n{msg}\n")
    for i in range(d, 0, -1):
        print(f"Clearing Screen in {i}", end='\r')
        stdout.write("\033[K")
        sleep(1)
    system('cls||clear')


def gu():
    """Function to greet the user"""
    print("\n\n\n\t\t\tHello user!")
    sleep(3)
    system('cls||clear')


if __name__ == "__main__":
    gu()
    print("\n\n\tWelcome to the basic formatted output functions in python!")
    print("\n\tFor more details about this module, ask Shantanu for the necessary information because he is too")
    print("\tlazy to write it himself!")
    clrscr('', 10)
    exitp("Good Bye!", 3)
