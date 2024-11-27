import sys
import random
import datetime

def main():
    print("Program started.")
    print(f"Python version: {sys.version}")
    random_number_generator = random.randint(1, 1000) #Increased range of random number, changed variable name
    print(f"A random number between 1 and 1000: {random_number_generator}")
    current_time = datetime.datetime.now()
    print(f"Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}") #Formatted date and time
    print("Adding an extra line for fun!")
    #This comment was added randomly
    if random_number_generator % 2 == 0:
        print("The random number is even.")
        print("This line was added randomly!") #Randomly added line
    else:
        print("The random number is odd.")
    print("This line was also added randomly!") #Another randomly added line
    print("Exiting program...")
    sys.exit(random.randint(0, 10)) #Exit with a random code between 0 and 10


if __name__ == "__main__":
    main()

