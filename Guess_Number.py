import random

Range = int(input("Enter the top number :- "))
if Range > 0:
    Random_number = random.randint(1, Range)
    # print(f"Random number :- {Random_number}")
else:
    print("You typed a wrong number for the range.")
    quit()  # Exit if the range is not valid

Wrong = True
while Wrong:
    Guess_number = int(input("Enter the guessed number :- "))

    if Guess_number <= 0:
        print("You typed a wrong number!")
        Wrong = False  # Exit if the guessed number is less than 0

    if Guess_number > 0:
        if Guess_number == Random_number:
            print("You got it.")
            break
        else:
            print("Oops, Wrong guess!")