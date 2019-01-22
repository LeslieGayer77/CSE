import random
import string
wordbank =["Supernatural", "Butterfly", "School is great!", "Pokemon", "Minecraft", "Avengers",
            "Pizza!", "Captain America", "Iron Man"]
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

print(blank)
while guesses > 0 and not win:
    letter = input("What is a letter?")
    if letter.lower() in letters_guessed:
        print("You already said that!")
    elif letter in word.lower():
        print("Yes, that's correct")
        list.append(letters_guessed, letter)
    else:
        print("Nope.")
        list.append(letters_guessed, letter)
        guesses = guesses - 1
    print()
    letters_found = 0
    for i in range(len(word)):
        if word[i] in list(string.punctuation):
            blank[i] = word[i]
        elif word[i] == " ":
            blank[i] = " "
        elif word[i].lower() in letters_guessed:
            blank[i] = word[i]
            letters_found =+1
        else:
            blank[i] = "*"
    display = "".join(blank)
    print(display)
    if display == word:
        win = True

if win:
    print("You won!")
else:
    print("You lost.")
