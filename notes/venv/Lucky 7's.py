#You lose 1 dollar each round. If the sum of the 2 dice is 7 then you get your money back plus 4.
money = 15
dice1 = 0
dice2 = 0
while money > 0:
    num = int(input("What are you betting?"))
    money = money - num
