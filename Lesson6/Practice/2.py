from collections import Counter

first_task = []
second_task = []
third_task = []
strk = []

Python = ['Ivan Ivanov', 'Petr Petrov', 'Sidor Sidorov', 'Kolobok Kolobkov']
FrontEnd = ['Ivan Chik', 'Ivan Petrov', 'Sidor Sidorov', 'Viktor Foo']
FullStack = ['Ivan Ivanov', 'Petr Petrov', 'Vasiliy Sai', 'Kung Foo']
Java = ['Peter Petrov', 'Aram Sidorov', 'Kolobok Kolobkov']

# студентов, которые учатся в двух и более группах
strk = Python + FrontEnd + FullStack + Java
c = Counter (list(map(lambda x: x, strk)))
for name, cnt in c.items():
    if cnt > 1:
        first_task.append(name)
print('Cтудентов в 2х и более группах -', first_task)

# студентов, которые не учатся на фронтенде
second_task = set(strk) | set(FrontEnd)
print('Студенты кроме FrontEnd -', second_task)

# студентов, которые изучают Python или Java
print('Python - ', Python)
print('Java - ', Java)
