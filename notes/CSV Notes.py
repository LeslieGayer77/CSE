import csv


def validate(num: str):
    if not all16digits(num):
        return False
    if devisableby3(num) and devisableby2(num):
        return True
    return False


def devisableby3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def devisableby2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file.....")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             Old_number = int(row[0]) + 1
#             old_number = row[0]
#             new_number = old_number = 1
#             row[0] = new_number
#             writer.writerow(row)
#
# print("OK")

# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file.....")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#
#         for row in reader:
#             # Old_number = int(row[0]) + 1
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#
# print("OK")


def reverse_it(string):
    print(string[::-1])


reverse_it("Hello World")
with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file.....")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)

        for row in reader:
            # Old_number = int(row[0]) + 1
            old_number = row[0]
            first_num = int(old_number[0])


def all16digits(num: str):
    if len(num) == 16:
        return True


list_num = list(number)
for index in range(len(list_num)):
    list_num[index] = int(list_num[index])