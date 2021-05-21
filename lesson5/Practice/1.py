stroka = 'nfdjJQNWEWQjnfa'
list_strok = ['s', 'a', 'B', 'C', 'sd', 'sA', ]
list_strok_2 = ['s', 'a', 'B', 'C', 'sd', 'sA', ]

def low_str():
    return stroka.lower()

def upper_str():
    return stroka.upper()

def niz(elm):
    return elm.lower()
low_list = list(map(niz, list_strok))

def verh(elm):
    return elm.upper()
up_list = list(map(verh, list_strok_2))


print(low_str())
print(upper_str())
print(low_list)
print(up_list)