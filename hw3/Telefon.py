print("Введите имя")
spravochnik_telefonov = {}

def spravochnik(spravochnik_telefonov):
    while True:
        name = str(input())
        if name != 'q':
            print("Введите номер телефона в формате +7-***-***-**-**")
            a = str(input())
            if a[0] == "+" and a[1] == "7" and a[2] == "-" and \
                a[6] == "-" and a[10] == "-" and a[13] == "-" and len(a) == 16 :
                if a[1:].replace("-", "").isdigit():
                    spravochnik_telefonov[name] = a
                    print("Введите имя")
                else:
                    print("Неправильный формат телефона, попробуйте снова")
                    print("Введите имя")
            else:
                    print("Неправильный формат телефона, попробуйте снова")
                    print("Введите имя")
        if name == 'q':
            print("Ващ справочник")
            print(spravochnik_telefonov)
            break


spravochnik(spravochnik_telefonov)