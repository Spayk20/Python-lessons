my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')
my_file1 =  open('numbers_result.txt', "w")

for j in range(20):               # Читаем файл в список
    data = my_file.readline()
    data = data.split()

    fizz = int(data[0])             # Присваиваем значения для переменных
    buzz = int(data[1])
    limit_number = int(data[2])
    
    print()
    res = ('')
    for i in range(1, limit_number+1):                     # Цикл проверки
        if not(i % fizz) and not(i % buzz):
            res += 'FB'
            print('FB', end = " ")
        elif not(i % fizz):
            res += 'F'
            print('F', end = " ")
        elif not(i % buzz):
            res += 'B'
            print('B', end = " ")     
        else:
            res += str(i)
            print(i, end = " ")
        res += ' '
    res += '\n'
    my_file1.write(res)     # запись в файл

my_file.close()
my_file1.close()