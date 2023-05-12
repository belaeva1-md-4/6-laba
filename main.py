def s():
    a={"Индия":"Нью-Дели", "Россия":"Москва", "Канада":"Оттава"}
    for key in a:
        print(key, "-", a[key])
    b=input("Введите страну  ")
    print(a[b])
    b=list(a)
    b.sort()
    print(b)

def s1():
    s=0
    d7={"Ф":10, "Щ":10, "Ъ":10}
    b=input()
    a=list(b)
    '''for x in d7.keys():
        if x in a:
            s=s+d7[x]'''
    for key, value in d7.items():
        if key in a:
            s=s+value
    print(s)

def s2():
    students = [
        {"name": "Иван", "languages": ["английский", "французский"]},
        {"name": "Мария", "languages": ["немецкий", "русский", "английский"]},
        {"name": "Петр", "languages": ["японский", "английский"]},
        {"name": "Анна", "languages": ["испанский", "итальянский", "французский", "китайский"]}
    ]
    langu = set()
    for student in students:
        langu.update(student["languages"])


    sorl = sorted(langu)
    print("Список всех языков:", sorl)

    chin = []
    for student in students:
        if "китайский" in student["languages"]:
            chin.append(student["name"])
    print("Студенты, знающие китайский язык:", chin)


s2()

