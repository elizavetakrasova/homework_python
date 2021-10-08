string = 'AAAbnAAbb'

def f1(string):
    string1 = string.lower()
    small, long = 0,0
    for i,j in zip(string,string1):
        if i == j:
            small +=1
        else:
            long +=1
    if small == long:
        return 0
    elif small > long:
        return -1
    else:
        return 1


print(f1(string))