data = []
my_file =  open(r'C:\Users\Я\Desktop\PYTHON\Less 3\HW\numbers.txt')



for j in range(20):               # Читаем файл в список
    data = my_file.readline()
    
    fizz = int(data[0])             # Присваиваем значения для переменных
    buzz = int(data[2])
    a = int(data[4]+data[5])
    
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