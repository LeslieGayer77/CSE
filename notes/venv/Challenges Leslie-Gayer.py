import math
#1
def challenge1 (Firstname, lastname):
    print(lastname, Firstname)
challenge1("Leslie", "Gayer")
print()

#2
def challenge2(num):
    factor = 0
    product = 0
    while factor < num and not product == num:
        factor = factor + 1
        product = factor * 2
    if product == num:
        return "$s is even" % num
    else:
        return "%s is not even" % num
print(challenge2(3))
print()

#3
def challenge3(b, h):
    return(b*h/2)
print(challenge3(3,4))
print()

#4
def challenge4(numm):
    if numm == 0:
        print("This number is zero")
    elif numm > 0:
        print("This number is positive")
    else:
        print("This number is negative")
print(challenge4(-3))
print()

#5
def challenge5(r):
    math.pi
    V = 4.0 / 3.0 * pi * r ** 3
    return V
print(challenge5(6))




