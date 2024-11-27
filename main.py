import sys
import random
import datetime

def main():
    print("Program started.")
    print(f"Python version: {sys.version}")
    random_number_generator = random.randint(1, 2000) #Increased range of random number, changed variable name and added a comment.  This is a completely arbitrary change.
    print(f"A random number between 1 and 2000: {random_number_generator}")
    current_time = datetime.datetime.now()
    print(f"Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}") #Formatted date and time
    print("Adding an extra line for fun!")
    #This comment was added randomly, and then I added another comment randomly.  This is completely arbitrary.
    print("Another randomly added line!") #Randomly added line
    if random_number_generator % 2 == 0:
        print("The random number is even.")
        print("This line was added randomly!") #Randomly added line
    else:
        print("The random number is odd.")
        print("This line was also randomly added!") #Another randomly added line, but this time with slightly different wording.  This is completely arbitrary.
    print("This line was also added randomly!") #Another randomly added line
    print("Exiting program...")
    sys.exit(random.randint(0, 20)) #Exit with a random code between 0 and 20.  This is a completely arbitrary change.


if __name__ == "__main__":
    main()

