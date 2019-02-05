import random
import string
wordbank = ["Supernatural", "Butterfly", "School is great!", "Pokemon", "Minecraft", "Avengers",
            "Pizza!", "Captain America", "Iron Man", "Awkward", "Cupcake", "Promiscuous", "Superstitious",
            "Goldfish", "koolaid", "Reaper", "Burgundy", "Military"]

win = False
letters_guessed = []
word = random.choice(wordbank)
guesses = 8
blank = []

for i in range(len(word)):
    if word[i] in list(string.punctuation):
        blank.append(word[i])
    elif word[i] == " ":
        blank.append(" ")
    else:
        blank.append("*")

print("Welcome to hangman")
print("You have 8 guesses, Good Luck!")
print()
while guesses > 0 and not win:
    letter = input("What is a letter?")
    print()
    if letter.lower() in letters_guessed:
        print("You already said that!")
    elif letter.lower() in word.lower():
        print("Yes, that's correct")
        list.append(letters_guessed, letter.lower())
    else:
        print("Nope.")
        list.append(letters_guessed, letter.lower())
        guesses = guesses - 1

    letters_found = 0
    for i in range(len(word)):
        if word[i] in list(string.punctuation):
            blank[i] = word[i]
        elif word[i] == " ":
            blank[i] = " "
        elif word[i].lower() in letters_guessed:
            blank[i] = word[i]
            letters_found = +1
        else:
            blank[i] = "*"
    display = "".join(blank)
    print(display)
    if display == word:
        win = True
    print("You have %s guesses left" % guesses)
    print("Letters Guessed %s" % letters_guessed)
    print()
if win:
    print("You won!")
    print("The word is %s" % word)
else:
    print("You lost.")
    print("The word was %s" % word)
print()
