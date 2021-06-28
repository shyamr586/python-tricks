from operator import itemgetter
from itertools import groupby, permutations

rows = [
    {"date": "07/01/2021", "client": "Manny", "paid":20},
    {"date": "07/01/2021", "client": "Pacquio", "paid":30},
    {"date": "07/02/2021", "client": "Roberto", "paid":10},
    {"date": "07/01/2021", "client": "Jack", "paid":70},
    {"date": "07/02/2021", "client": "Sparrow", "paid":0},
    {"date": "07/03/2021", "client": "Damian", "paid":10},
    {"date": "07/04/2021", "client": "Sam", "paid":70},
    {"date": "07/03/2021", "client": "Darko", "paid":7}
]

rows.sort(key=itemgetter("date"))               # the attribute to be grouped must be sorted first

for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print ("\t",i)
    print("")