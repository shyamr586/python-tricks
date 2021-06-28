from operator import itemgetter                         # as name suggests, helps in getting an item easily

rows = [
    {"name": "Mith", "amount": 100000, "rank": 2},
    {"name": "Shy", "amount": 50000000000, "rank": 1},
    {"name": "Cler", "amount": 70000, "rank": 3},
    {"name": "Ayaan", "amount": -1, "rank": 7500000000}
]


rows.sort(key=itemgetter("rank"))
print (rows)

rows.sort(key=itemgetter("name"))
print("\n")
print (rows)

rows.sort(key=itemgetter("amount"), reverse=True)
print ("\n")
print (rows)

# rank_sorted = sorted(rows, key=itemgetter("rank"))
# name_sorted = sorted(rows, key=itemgetter("name"))
# amount_sorted = sorted(rows, key=itemgetter("amount"))

# print (itemgetter)

# print (rank_sorted)
# print("\n")
# print (name_sorted)
# print("\n")
# print (amount_sorted)

