
print("Hello world")

#this is a comment
#1. make notes to myself
#2. Comment pieces of code that do not work
#3. make my code easier to read

print ("Look at what happens her. Is there any space?")
print()
print()
print ("There should be a couple blank lines here.")

#math
print (3+5)
print (5-2)
print (3*4)
print (6/2)

print("Figure this out...")
print (6//2)
print (5//2)
print (9//4)
# // = take off the extra part after the decimal

print ("here is another one")
print (6%2)
print (5%2)
print (11%4)
# modulus (Remainder)

#Powers
# What is 2^20
print(2**4)
print(3**27)

#Taking input
name = input ("What is your name?")
print("Hello %s" % name)

age = input ("How old are you? >_")
print ("%s?!? You belong in a museum." % age)
print()
print("%s IS REALLY OLD. She IS %s YEARS OLD." % (name, age))

# Variable Assignments
car_name = "Baby"
car_type = "1967 Chevy Impala Sport Sedan"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Baby. It is a tesla."
print("I have a car called %s. It is a %s." % (car_name, car_type))

#Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)


"""
This is a multi-line comment
anything between the "s is not run
"""


#functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()

# f(X) = 2x + 3
def f(x):
    print(2*x + 3)
f(1)
f(5)
f(5000)

print()

# Distance Formula
def distance(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y2-y1)**2)**(1/2)
    print(dist)

distance(0,0,3,4)
distance(0,0,5,12)

#Loops
for i in range(5): # This gives the numbers 0-4
    say_it()

for i in range(10):
    print(i)


for i in range(5): #This is going back to the f(x)=2x+3
    f(i)
print()
#while loops
a = 1
while a < 10:
    print(a)
    a += 2  # This is the same as saying a = a + 1

guesses = 5

"""
At the moment you START the loop:
Fir loops - Use when you know EXACTLY how many interations
While loops - Use when you DONT know how many iterations
"""

print()

# Control structures (If statements)
sunny = False
if sunny:
    print("Go Outside!")

def grade_calc(percentage):
    if percentage >=90:
        return "A"
    elif percentage >=80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

print()

# "Random" Notes
import random   # This should be on line one
print(random.randint(0, 100))

print()

# Equality Statements
print(5>3)
print(5>=3)
print(3==3)
print(3!=4)
"""
a=3 # A is set to 3
a==3 # Is a equal to 3
"""
print()
print()
#Creating Lists
colors = ["black", "red", "turquoise", "pink", "blue", "burgundy", "charcoal", "green", "white", "grey"]
print(colors)
print(colors[1])
print(colors[0])

#length of list
print("There are %d things in the list" % len(colors))

#Changing elements in a list
colors[3] = "Orange"
print(colors)

#Looping through lists
for item in colors:
    print(item)

print()
print()
"""
1. Make a list with 7 items
2. Change the third thing in the list
3. Print the item
4. Print the full list
"""

names = ["Jensen", "Jared", "Misha", "Justin", "Jeremy",
         "James", "Jackson"]
names[2] = "Dean"
print(names[2])
print()
for item in names:
    print(item)
print("The last thing in the list is %s" % names[len(names)-1])
#len = length
print()
print()
#slicing a list
print(names[1:3])
print(names[1:4])
print(names[1:])
print(names[:4])

print()
print()

food_list = ["pizza", "tacos", "pie", "meat", "salad", "chips", "burrito", "macarroni", "sushi",
             "rice", "noodles", "icecream", "cookies", "chicken", "chocolate", "waffles", "water", "ramen", "bleach",
             "hamburger", "candy"]

print(len(food_list))
print(food_list[13])

#adding stuff to the list
food_list.append("bacon")
food_list.append("eggs")
#notice that everything is object.method(parameters)

food_list.insert(1, "eggo waffles")

#removing things
food_list.remove("salad")
print(food_list)

print()

care = ["jay","jar","jen"]
care.append("mish")
care.remove("jay")
print(care)

#tuples
bramds = ("apple", "samsung", "HTC",) #PARENTHESIS
print()
#also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

print()
#frind the index of an item
print(food_list.index("chicken"))

print()
#changing thingnto a list
string1 = "black"
list1 = list(string1)
print(list1)

for i in range(len(list1)): # i goes through all indicies
    if list1[i] == "a": #if we find a
        list1.pop(i) # remove the i-th index
        list1.insert(i, "*")

#turning a list into a string
print("".join(list1))

"""
for character in list1:
    if character == "a":
    #replace with a *
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")
"""
print()
#function notes
#a**2 + b**2 = c**2
def pythagorean(a, b):
    return(a**2 + b**2)**(1/2)

print(pythagorean(3,4))