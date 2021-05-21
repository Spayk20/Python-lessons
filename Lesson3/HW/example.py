import re
res = str()
my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')

for _ in range(20):
    data = my_file.readline()     # Читаем файл в строку
    num_list = re.findall('\d+', data)      # Ищем все числа и записываем их в список
   
    fizz = int(num_list[0])             # Присваиваем значения для переменных
    buzz = int(num_list[1])
    a = int(num_list[2])
    
    print(num_list)


my_file.close()