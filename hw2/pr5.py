import random

names = ['Ivan', 'Petr']
sec_names = ['Ivanovich','Petrovich']
sur_names = ['Ivanov', 'Petrov']

def get_names(names,sec_names, sur_names, num):
    result = []
    i = 0
    while i<num:
        new_n = random.choice(names)
        new_sn = random.choice(sec_names)
        new_sur = random.choice(sur_names)
        name = new_n + ' ' + new_sn + ' ' + new_sur + ' '
        result+=name
        i+=1
    return result

print(get_names(names,sec_names, sur_names, 2))