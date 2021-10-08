list1=[1,2,3,3,4,4,5,5]

def f1(list1):
    for i in set(list1):
        if list1.count(i)>1:
            print(i, "повторяется", list1.count(i), "раз(а)")

print(set(list1))
f1(list1)
