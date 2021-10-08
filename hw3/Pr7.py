import string 

def stri(string1):
    d={}
    for name in string.ascii_letters:
        d[name] = string1.count(name)
    return d

string1 = 'aabbccdd'
print(stri(string1))
        