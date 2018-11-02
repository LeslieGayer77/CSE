passage = ("Lets Go Tigers!")
guesses = 10
while guesses > 0:
    letter = (input("What's a letter?"))
    if letter == "A" or "B" or "C" or "D" or "F" or "H" or "J" or "K" or "L" or "N" or "M" or "P" or "Q" or "U" or "V" or "W" or "X" or "Y" or "Z":
        print("Nope. minus one guess")
        guesses = guesses - 1
    if letter == "L" or "E" or "T" or "S" or "G" or "O" or "I" or "R":
        print("Yep!")

print("Lets Go Tigers!")