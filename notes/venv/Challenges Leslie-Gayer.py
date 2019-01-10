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
    A = math.pi * r ** 2
    return A
print(challenge5(4))
print()

#6
def challenge6(r):
    V = 4.0 / 3.0 * math.pi * r ** 3
    return V
print(challenge6(2))
print()

#7
def challenge7(n):
    A = n + n**2 + n**3
    return A
print(challenge7(2))
print()

#8
def challenge8(nam):
    if nam >= 1850 and nam <= 2150:
        return "This is within 150 of 2,000"
    elif nam >= 2850 and nam <= 3150:
        return "This is within 150 of 3,000"
    else:
        return "No, This is not 150 within 2,000 or 3,000"
print(challenge8(1900))
print()


