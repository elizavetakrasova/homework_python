name = str(input())
def initials(name):
    wl = name.split()
    return wl[0]+' '+ wl[1][0] + '.' + wl[2][0] + '.' 
print(initials(name))