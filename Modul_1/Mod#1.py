    # Функция получает на вход массив строк. Вернуть надо количество строк,
    # которые не короче двух символов и у которых первый и последний
    # символ совпадают.

words = ('aba', 'xyz', 'aa', 'x', 'bbb')

count = 0
for slovo in words:
    if (len(slovo) >= 2) and (slovo[0] == slovo[-1]):
        count += 1
print(count)