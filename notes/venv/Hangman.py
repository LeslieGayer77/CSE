import random

word_bank = ["cat", "box", "dog"]
word = random.choice(word_bank)
letters_correct = []
letters_incorrect = []
guesses = 10
while guesses > 0:
    letter = (input("What's a letter?"))
    if letter.lower() in letters_correct:
        print("Yes, that's in the word, but you already said that!")
    elif letter in word:
        print("Yes, that's correct")
        list.appends(letters_correct, letter)
        guesses = guesses - 1
    elif letter.lower() in letters_incorrect:
        print("You already tried that letter;it was wrong.")
    else:
        print("Nope.")
        list.append(letters_incorrect, letter)
        guesses = guesses - 1
    print("%s guesses left" % guesses)
    print()

print("The word was %s" % word)


"""passage = ("Lets Go Tigers!")

    if letter == "A":
        print("Nope")
        guesses = guesses - 1
    elif letter == "B":
        print("Nope")
        guesses = guesses - 1
    elif letter == "C":
        print("Nope")
        guesses = guesses - 1
    elif letter == "D":
        print("Nope")
        guesses = guesses - 1
    elif letter == "F" :
        print("Nope")
        guesses = guesses - 1
    elif letter == "H":
        print("Nope")
        guesses = guesses - 1
    elif letter == "J":
        print("Nope")
        guesses = guesses - 1
    elif letter == "K":
        print("Nope")
        guesses = guesses - 1
    elif letter == "N":
        print("Nope")
        guesses = guesses - 1
    elif letter == "M":
        print("Nope")
        guesses = guesses - 1
    elif letter == "P":
        print("Nope")
        guesses = guesses - 1
    elif letter == "Q":
        print("Nope")
        guesses = guesses - 1
    elif letter == "U":
        print("Nope")
        guesses = guesses - 1
    elif letter == "V":
        print("Nope")
        guesses = guesses - 1
    elif letter == "W":
        print("Nope")
        guesses = guesses - 1
    elif letter == "X":
        print("Nope")
        guesses = guesses - 1
        
    elif letter == "Y":
        print("Nope")
        guesses = guesses - 1
    elif letter == "Z":
        print("Nope")
        guesses = guesses - 1
    elif letter == "L":
        print("Yep!")
    elif letter == "E":
        print("Yep!")
    elif letter == "T":
        print("Yep!")
    elif letter == "S":
        print("Yep!")
    elif letter == "G":
        print("Yep!")
    elif letter == "O":
        print("Yep!")
    elif letter == "R":
        print("Yep!")
    elif letter == "I":
        print("Yep!")
    
print("Lets Go Tigers!")"""