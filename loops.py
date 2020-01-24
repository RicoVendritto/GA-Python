items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
item_len = len(items)
print(item_len)

for i in items:
    print(i)

for i in range(4):
    print(items[i])

for i in range(1, item_len, 2):
    print(items[i])

items2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for i in range(1, len(items2) - 1, 2):
    print(items2[i])
