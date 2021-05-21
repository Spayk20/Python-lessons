import re                   # подключаем библиотеку регулярных выражений
my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')

              
data = my_file.readline()     # Читаем файл в строку
num_list = re.findall('\d+', data)      # Ищем все числа и записываем их в список
   
fizz = int(num_list[0])             # Присваиваем значения для переменных
buzz = int(num_list[1])
a = int(num_list[2])
    
print()
for i in range(1, a+1):                     # Цикл проверки
    if not(i % fizz) and not(i % buzz):
        print('FB', end = " ")
    elif not(i % fizz):
        print('F', end = " ")
    elif not(i % buzz):
        print('B', end = " ")     
    else:
        print(i, end = " ")

my_file.close()