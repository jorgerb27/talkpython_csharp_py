import random
from itertools import count


def main():
    show_header()

    the_number = random.randint(1, 100)

    count = 0
    while True:
        guess = get_guess()
        if not guess:
            continue

        count += 1
        if evaluate_guess(guess, the_number):
            break

    print(f"you guessed in {count} attempts!")
def evaluate_guess(guess, the_number):
    if guess == the_number:
        print(f"you guessed the number {guess}!")
    if guess < the_number:
        print(f"That's too LOW!")
    if guess > the_number:
        print(f"That's too HIGH!")
    return guess == the_number

def get_guess():
    try:
        text = input("enter your guess: ")
        val = int(text)
        if val < 1 or val > 100:
            print("invalid input")
            return None
        return val
    except:
        print("you didn't enter a number")

def show_header():
    print("-------------------------------------------")
    print("|                                         |")
    print("|           Py HIGH / LOW GAME            |")
    print("|                                         |")
    print("-------------------------------------------")
    print()
    print("I'm thinking of a number between 1 & 100.")
    print("How many steps can you guess it in?")
    print()


if __name__ == '__main__':
    main()