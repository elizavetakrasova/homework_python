name_list = ['ahhaah jahjah ajhajh','agfaga ahgaha ahajah']

def initials(name):
    wl = name.split()
    return wl[0]+' '+ wl[1][0] + '.' + wl[2][0] + '.' 

def initials_list(names_list):
    return [initials(name) for name in names_list]

print(initials_list(name_list))
