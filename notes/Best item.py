import csv


with open("Sales Records.csv", 'r') as old_csv:
        reader = csv.reader(old_csv)
        for row in reader:
            Regions = row[0]
            countries = row[1]
            snacks = row[2]
            onanoff = row[3]
            order_priority = row[4]
            order_date = row[5]
            order_id = row[6]
            ship_date = row[7]
            unit_sold = row[8]


            print(row[3])
