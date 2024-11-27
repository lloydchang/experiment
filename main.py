import sys
import random
import datetime

def new_random_function():
    """This function returns a random fruit."""
    return random.choice(["apple", "banana", "cherry", "date", "fig"])

def main():
    print("Program started!")
    print(f"Python version: {sys.version}")
    myRandomNumber = random.randint(1, 1000) # Changed variable name
    print(f"A random number between 1 and 1000: {myRandomNumber}")
    current_time = datetime.datetime.now()
    print(f"Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    #This line has been commented out!
    #print("This line has been randomly added!")
    if myRandomNumber % 2 == 0:
        print("The random number is even.")
        print("Another random line added here!")
        fruit = new_random_function()
        print(f"Random fruit: {fruit}")
        print("Added another line for fun!")
    else:
        print("The random number is odd.")
        print("This line is also randomly added.")
        print("And another one!")

    print("Exiting program...")
    sys.exit(0)


if __name__ == "__main__":
    main()
