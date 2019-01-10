import random
wordbank = ["Supernatural", "Butterfly", "School", "School is great!", "Pokemon", "Minecraft", "Avengers",
            "Pizza!", "Captain America", "Iron Man"]

word = random.choice(wordbank)
print(word)
win = False
letters_guessed = []
letters_incorrect = []
letters_required = 0
guesses = 8



guess = input("What is a letter?")
