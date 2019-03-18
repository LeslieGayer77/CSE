import random
 # You lose 1 dollar each round. If the sum of the 2 dice is 7 then you get your money back plus 4.
money = 15
dice1 = 0
dice2 = 0
lose = True
round = 1
highscore = 0
best_round = 0
while money > 0:
    print("Round %s" % round)
    num = int(input("What are you betting?"))
    money = money - num
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("You got 7!")
        print("+ %s" % num)
        money = money + num + 4
    elif not dice1 + dice2 == 7:
        print("Sorry you rolled %s and %s" % (dice1, dice2,))
        print("- %s" % num)
    print("You have %s dollars left" % money)
    print()
    if highscore < money:
        highscore = money
        best_round = round
    round = round + 1
print("You lasted %s Rounds" % round)
print("You should have stopped when you had %s in round %s" % (highscore, best_round))
print()
if lose == True:
    print("You dont have anymore money")
