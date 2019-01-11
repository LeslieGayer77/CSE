import random
wordbank = ["Supernatural", "Butterfly", "School", "School is great!", "Pokemon", "Minecraft", "Avengers",
            "Pizza!", "Captain America", "Iron Man"]

win = False
letters_guessed = []
letters_incorrect = []
letters_found = 0
word = random.choice(wordbank)
letters_required = len(word)
guesses = 8

while guesses > 0 and not letters_found == letters_required:
    letter = input("What is a letter?")
