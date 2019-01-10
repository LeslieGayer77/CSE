import random
#Guess Game
number = random.randint(1, 100)

guesses = 10
win = False
while guesses > 0:
    num = int(input("What's a number from 1 to 100?"))
    print()
    if num >= 101:
        print("WAY TOO HIGH. Follow the directions")
        guesses = guesses - 1
        print("You have %s guesses left" % guesses)
    elif num > number:
        print("a little lower")
        guesses = guesses - 1
        print("You have %s guesses left" % guesses)
    elif num < number:
        print("a little higher")
        guesses = guesses - 1
        print("You have %s guesses left" % guesses)
    elif num == number:
        print("Correct")
        guesses = 0
        win = True
        print("You have %s guesses left" % guesses)
print()
if win:
    print("You Win!")
else:
    print("You lose.")

print("Game end.")





