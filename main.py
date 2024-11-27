import sys

def main():
    print("Program is about to exit...")
    print(f"Python version: {sys.version}") #Added this line
    print("Exiting program...")
    #Added a comment for demonstration purposes.
    sys.exit(0)  # Exit with a success code

if __name__ == "__main__":
    main()
