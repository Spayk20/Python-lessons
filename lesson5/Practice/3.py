from collections import Counter

my_file = open(r'C:\Users\Я\Desktop\PYTHON\Урок 5\Практика\text.txt')
txtx = my_file.readline()
txtx = txtx.split()

c = Counter (list(map(lambda x: x.lower(), txtx)))
print(c)

my_file.close()