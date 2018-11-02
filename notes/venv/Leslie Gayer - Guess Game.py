#Guess Game
number = 7
guesses = 5
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
    elif num == 7:
        print("Correct")
        guesses = 0
print()
if guesses == 0:
    print ("You lose")

print("Game end.")





