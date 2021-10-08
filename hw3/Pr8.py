text = 'слово слово слово привет привет привет как как как о о о кек кек кек лол лол лол хей хей хей\
    хоп хоп хоп дд дд дд ррр ррр ррр ло алао вало дыфоваа алооло'

def f1(text):
    d={}
    a=[]
    for name in text.split():
        d[name] = text.split().count(name)
    a = sorted(d.items(), key=lambda x:x[1], reverse = True)
    for i in range(10):
        print(i+1, 'слово', a[i][0], 'количество повторений', a[i][1], "раз(а)")

print('ТОП 10 СЛОВ')
f1(text)
