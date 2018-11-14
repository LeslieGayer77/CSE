import random
#Guess Game
number = random.randint(1, 10)

guesses = 5
win = False
while guesses > 0:
    num = int(input("What's a number from 1 to 10?"))
    if num >= 11:
        print("WAY TOO HIGH. Follow the directions")
        guesses = guesses - 1
    elif num > number:
        print("a little lower")
        guesses = guesses - 1
    elif num < number:
        print("a little higher")
        guesses = guesses - 1
    elif num == number:
        print("Correct")
        guesses = 0
        win = True
print()
if win:
    print("You Win!")
else:
    print("You lose.")

print("Game end.")





