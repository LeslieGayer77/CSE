import csv
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10
# (Modulo 10)


def all16digits(num: str):
    if len(num) == 16:
        print("All the digits are 16 numbers long")
        return True
    return False


def drop_last_digit(num: str):
    return num[:14]


def reverse_it(string):
    return string[::-1]


def addnums(nums: list):
    sum_num = 0
    for index in range(len(nums)):
        sum_num += int(nums[index])
    return sum_num


def multiply(num):
    list_num = list(num)
    for index in range(len(list_num)):
        if index % 2 == 0:
            list_num[index] = int(list_num[index])
            list_num[index] *= 2
            if list_num[index] > 9:
                list_num[index] -= 9
    return addnums(list_num)


def validate_card_number(num: str):
    if not all16digits(num):
        print("This number is not 16 digits. It is not valid.")
        return False
    if not multiply(reverse_it(drop_last_digit(num))) % 10 == num[15]:
        print("This number is not valid")
        return False
    print("This number is valid")
    return True


multiply(reverse_it(drop_last_digit("5431709304959590")))
validate_card_number("5431709304959590")

with open("Book1.csv", 'r') as old_csv:
    with open("invalid_numbers.csv", 'w', newline='') as new_csv:
        print("Writing file.....")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            # Old_number = int(row[0]) + 1
            old_number = row[0]
            if not validate_card_number(old_number):
                print(old_number, "is not valid")
                writer.writerow(row)
