import random 

def gen_names(names, second_names, sur_names, num):
    i = 0 
    while i < num:
        yield random.choice(names) + " " + random.choice(second_names) + " " + random.choice(sur_names)
        i += 1

for i in gen_names( ["Красова", "Свиридова", "Некрасова"], \
    ["Елизавета", "Екатерина", "Анастасия"], \
    ["Александровна", "Дмитриевна", "Николаевна"], 3):
    print(i)
