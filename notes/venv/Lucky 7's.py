import random
#You lose 1 dollar each round. If the sum of the 2 dice is 7 then you get your money back plus 4.
money = 15
dice1 = 0
dice2 = 0
lose = False
while money > 0:
    num = 1
    money = money - num
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        print("You got 7!")
        print("+ %s" % num)
    elif not dice1 + dice2 == 7:
        print("Sorry - %s" % num)
    elif money == 0:
        lose = True

print()
if money == 0:
    print("You dont have anymore money")
