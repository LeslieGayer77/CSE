import csv
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10
# (Modulo 10)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file.....")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)

        for row in reader:
            # Old_number = int(row[0]) + 1
            old_number = row[0]
            first_num = int(old_number[0])
            last_num = int(old_number[15])
            num15 = 


def all16digits(num: str):
    if len(num) == 16:
        print("All the digits are 16 numbers long")
        return True
    return False


def drop_last_digit:
    last_num


def reverse_it(string):
    print(string[::-1])


def multiply(num):
    list_num = list(number)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])



def validate_card_number(num: str):


print(all16digits("5431709304959590"))