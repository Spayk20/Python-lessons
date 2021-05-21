import re
res = str()
my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')
my_file1 =  open('numbers_result.txt', "w")

data = my_file.readline()     # Читаем файл в строку
num_list = re.findall('\d+', data)      # Ищем все числа и записываем их в список
   
fizz = int(num_list[0])             # Присваиваем значения для переменных
buzz = int(num_list[1])
a = int(num_list[2])
    
for i in range(1, a+1):                     # Цикл проверки
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

my_file1.write(res)     # запись в файл

my_file.close()
my_file1.close()