fizz = int(input())
buzz = int(input())
a = int(input())
for i in range(1, a+1):
    if not(i % fizz) and not(i % buzz):
        print('FB', end = " ")
    elif not(i % fizz):
        print('F', end = " ")
    elif not(i % buzz):
        print('B', end = " ")     
    else:
        print(i, end = " ")