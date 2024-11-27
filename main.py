import sys
import random
import datetime

def main():
    print("Program started.")
    print(f"Python version: {sys.version}")
    random_number = random.randint(1, 1000) #Increased range of random number
    print(f"A random number between 1 and 1000: {random_number}")
    current_time = datetime.datetime.now()
    print(f"Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}") #Formatted date and time
    print("Adding an extra line for fun!")
    if random_number % 2 == 0:
        print("The random number is even.")
        print("This line was added randomly!") #Randomly added line
    else:
        print("The random number is odd.")
    print("Exiting program...")
    sys.exit(random.randint(0, 10)) #Exit with a random code between 0 and 10


if __name__ == "__main__":
    main()

