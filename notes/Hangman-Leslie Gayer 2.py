import random
import string
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
wordbank = ["Supernatural", "Butterfly", "School", "School is great!", "Pokemon", "Minecraft", "Avengers",
            "Pizza!", "Captain America", "Iron Man"]

win = False
letters_guessed = []
letters_incorrect = []
letters_correct = []
letters_found = 0
word = random.choice(wordbank)
letters_required = len(word)
guesses = 8

while guesses > 0 and not letters_found == letters_required:
    letter = input("What is a letter?")
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
            print("si")
