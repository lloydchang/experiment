import sys
import random
import datetime

def main():
    print("Program is about to exit...")
    print(f"Python version: {sys.version}")
    random_number = random.randint(1, 100)
    print(f"A random number: {random_number}")
    print("This line is randomly added and will likely cause issues.")
    print(f"Current date and time: {datetime.datetime.now()}") #Added line
    print("Exiting program...")
    #Added a comment for demonstration purposes.
    #Randomly choose exit code
    if random.random() < 0.5:
        sys.exit(0) #Exit with code 0
    else:
        sys.exit(random_number % 2)  # Exit with a random success/failure code

if __name__ == "__main__":
    main()
