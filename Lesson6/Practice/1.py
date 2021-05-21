dct = {'John Deere' : [3, 3, 5], 'Austin Powers' : [3, 3, 5], 'Mustafa Ilim' : [5, 4, 3]}
lst = list()
best = list()
worst = list()

for x in dct:
    cred_ball = sum(dct[x]) / len(dct[x])
    dct[x] = cred_ball

# lst = sorted(dict.items(dct))
# print(lst)

vishaya_ocenka = max(dct.values())
nizshaya_ocenka = min(dct.values())
print(vishaya_ocenka)
print(nizshaya_ocenka)

for name, ball in dct.items():
    if ball == vishaya_ocenka:
        best.append(name)
    elif ball == nizshaya_ocenka:
        worst.append(name)
print('Лучший студент -', best)
print('Худший студент -', worst)