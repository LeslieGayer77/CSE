import csv


with open("Sales Records.csv", 'r') as old_csv:
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[0]
            print(old_number)