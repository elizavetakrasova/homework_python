list1=[[1,2,3],[1,2,3,4,5],[1,3,4],[1,4,5,6]]

def f1(list1):
    s1 = set(list1[0])
    for i in list1[1:]:  
        s1.intersection_update(set(i))
    return list(s1)

print(f1(list1))


