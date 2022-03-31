import csv

# def csv_reader(*args):
#     for elem in args:
#         with open(elem) as file:
#             csv_text = csv.reader(file)
#             for el in csv_text:
#                 print(el)
#         print('\n\n\n ')

elem = input("Enter the name of the csv file >>>")

if '.' not in elem:
        elem = elem + '.csv'


with open(elem) as file:
    csv_text = csv.reader(file)
    next(csv_text)
    for el in csv_text:
        # print(el)
        print(f"{el[1]}({el[0]}-y.) costs {el[4]}")
# csv_reader('text.csv','text2.csv')

