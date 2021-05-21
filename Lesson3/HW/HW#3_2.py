data = []
my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')



for j in range(20):               # Читаем файл в список
    data = my_file.readline()
    data = data.split()

    fizz = int(data[0])             # Присваиваем значения для переменных
    buzz = int(data[1])
    limit_number = int(data[2])
    
    print()
    for i in range(1, limit_number+1):                     # Цикл проверки
    	if not(i % fizz) and not(i % buzz):
        	print('FB', end = " ")
    	elif not(i % fizz):
        	print('F', end = " ")
    	elif not(i % buzz):
       		print('B', end = " ")     
    	else:
        	print(i, end = " ")

my_file.close()