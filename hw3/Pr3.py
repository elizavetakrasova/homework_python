s1=[1,2,3,4]
s2=[3,4,5,6]
def f1(s1,s2):
    s1=set(s1)
    s2=set(s2)
    return list(s1.intersection(s2))
print(f1(s1,s2))