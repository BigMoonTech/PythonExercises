import random

random_num = random.randint(1,10)
isPlaying = True

while isPlaying:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == random_num:
        print("You win!")
        while True:
            choice = input("Do you want to play again? (y/n) ").lower()
            if choice == "n":
                isPlaying = False
                break
            elif choice == "y":
                random_num = random.randint(1,10)
                break
            else:
                print("Invalid answer.")
    elif guess > random_num:
        print("Too high, try again.")
    else:
        print("Too low, try again.")


