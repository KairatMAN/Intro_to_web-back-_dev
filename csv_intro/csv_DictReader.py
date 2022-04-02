import csv

with open ('text.csv') as file:
    csv_Reader = csv.DictReader(file)
    csv_Reader1 = csv.reader(file)
    # next(csv_Reader)
    for el1 in csv_Reader1:
        print(el1)

    for el in csv_Reader:
        print(el)

