s = str('History is the study of the past. Events occurring before the invention of writing systems are considered prehistory. "History" is an umbrella term that relates to past events as well as the memory, discovery, collection, organization, presentation, and interpretation of information about these events.')
s_fr = str()
s_cmprh = str()
s_rep = str()


for elem in s:
    if elem != 'a':
        s_fr += elem


s_cmprh = ''.join([elem for elem in s if elem != 'a'])


s_rep = s.replace('a','')


index_last = s.rindex('discovery')


print('FOR - ', s_fr)
print('List compr -', s_cmprh)
print('REPLACE - ', s_rep)
print('Poslednyay_stroka - ', s[index_last:])
print()
print("""History is the study of the past. Events occurring before the invention of writing systems are considered prehistory.
"History" is an umbrella term that relates to past events as well as the memory, discovery, collection, organization, presentation, and interpretation of information about these events.""")