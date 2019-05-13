import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    items = {}
    for row in reader:
        # Regions = row[0]
        # countries = row[1]
        # item = row[2]
        # order_priority = row[4]
        # onanoff = row[3]
        # order_date = row[5]
        # order_id = row[6]
        # ship_date = row[7]
        # unit_sold = row[8]
        # profit = row[13]
        if not row[11] == 'Total Revenue':
            item = row[2]
            try:
                items[item]["REVENUE"] += float(row[11])
                items[item]["UNITS_SOLD"] += int(row[8])
                items[item]["BENEFIT"] = items[item]["REVENUE"] / items[item]["UNITS_SOLD"]
            except KeyError:
                print()
                print(item)

                items[item] = {"NAME": item, "REVENUE": float(row[11]), "UNITS_SOLD": int(row[8]),
                               "BENEFIT": float(row[11]) / int(row[8])}
    print("CALCULATING NUMBER STUFF")
    top_benefit = items[item]
    for thingy in items:
        if items[thingy]["BENEFIT"] > top_benefit["BENEFIT"]:
            print(items[thingy]["NAME"], "is better than", top_benefit["NAME"])
            top_benefit = items[thingy]
    print("Clearly, the best thing to sell is", top_benefit["NAME"])
