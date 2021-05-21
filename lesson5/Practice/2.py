x = 6
spisok_chisel = [2, 3, 5, 4, 7, 11]
kvadrat_prostih = []


def kvad():
    return x ** 2


for item in spisok_chisel:
    k = 0
    for i in range(1, item+1):
        if (item % i == 0):
            k = k + 1
    if (k == 2):
        kvadrat_prostih.append(item ** 2)


print(kvad())
print(kvadrat_prostih)