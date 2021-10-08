import random
lenn = int(input())
n, m = map(int,input().split())

def f1(lenn, n ,m):
    a=[]
    for i in range(lenn):
        a.append(random.randint(n,m))
    return a

print(f1(lenn, n, m))

def sort1():
    a2 = [10,9,8,7,6,5,4,3,2,1]
    for i in range(len(a2)):
        for j in range(len(a2)-1):
            if a2[j] > a2[j+1]:
                a2[j], a2[j+1] = a2[j+1], a2[j]
    return a2

print(sort1())