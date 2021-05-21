smma = int(input())
a = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = 0

i = 0
for item in a: 
    count = smma // item
    smma %= item
    print(item, '-', count)
