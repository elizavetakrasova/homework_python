import random

def get_names(num):
    names = ['Ivan', 'Petr']
    sec_names = ['Ivanovich','Petrovich']
    sur_names = ['Ivanov', 'Petrov']
    for i in range (num):
        names1 = random.choice(names)
        sec_names1 = random.choice(sec_names)
        sur_names1 = random.choice(sur_names)
        person = names1 + sec_names1 + sur_names1
        return person
        

print(get_names(2))