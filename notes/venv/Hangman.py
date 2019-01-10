import random

letters_correct = []
letters_incorrect = []
letters_found = 0
letters_required = 0
doubles = 0
guesses = 10
list = output
word_bank = ["supernatural", "superstituous", "bangbang", "mynamesjeff", "koolaid",
     "darkness", "friends", "night", "reaper", "goldfish", "woah", "selectively",]
word = random.choice(word_bank)
letters_required = len(word)
counting_letters = []

for i in range(len(word)):
    count = word.count(word[i])
    if word[i] in counting_letters:
       print()
    elif count > 1:
        count = count - 1
        doubles = doubles + count
    list.append(counting_letters, word[i])

letters_required = len(word) - doubles

# print(doubles)
#print(word)
#print("%s doubles" % doubles)
#print("%s letters needed" % letters_required)

while guesses > 0 and not letters_found == letters_required:
    letter = (input("What's a letter?"))
    if letter.lower() in letters_correct:
        print("Yes, that's in the word, but you already said that!")
    elif letter in word.lower():
        print("Yes, that's correct")
        list.append(letters_correct, letter)
        letters_found = letters_found + 1
    elif letter.lower() in letters_incorrect:
        print("You already tried that letter; it was wrong.")
    else:
        print("Nope.")
        list.append(letters_incorrect, letter)
        guesses = guesses - 1
    print()
    for i in range(len(word)):  # Listing correct letters
        if (word[i]) in letters_correct:

        else:
            print(".")

    print()
    print("%s guesses left" % guesses)
    print()
    print("You found %s letters" % letters_found)

print("The word was %s" % word)
if letters_found == letters_required:
    print("You won!")
else:
    print("You lost.")

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