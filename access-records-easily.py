# in order search for a group of records by a field like 'date', we use this method.

from collections import defaultdict

rows_by_date = defaultdict(list)            #using this we can easily access or search for a record

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

for row in rows:
    rows_by_date[row["date"]].append(row)

tot = 0
for r in rows_by_date["07/01/2021"]:
    print (r)
    tot+=r['paid']
print ("Total price paid in 07-01-2021 is:",tot)