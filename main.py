# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def filetodict(file, sep=' | '):
    tmplist = list()
    cook_book = {}
    tl3 = list()
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            if line != '\n':
                tmplist.append(line.replace('\n', ''))
            else:
                for i in range(2, len(tmplist)):
                    tl2 = tmplist[i].split(sep)
                    tl3.append({'ingredient_name': tl2[0], 'quantity': int(tl2[1]), 'measure': tl2[2]})
                cook_book.update({tmplist[0]: tl3})
                tmplist = list()
                tl3 = list()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    tmplist = []
    tmpdict = {}
    for i in cook_book:
        if dishes.count(i) > 0:
            for j in cook_book[i]:
                for k in tmplist:
                    if k['ingredient_name'] == j['ingredient_name']:
                        tmplist[tmplist.index(k)]['quantity'] += j['quantity']
                        tmplist[tmplist.index(k)]['quantity'] *= person_count
                        break
                else:
                    j['quantity'] *= person_count
                    tmplist.append(j)
    for i in tmplist:
        ti = i['ingredient_name']
        i.pop('ingredient_name')
        tmpdict.update({ti: i})
    return tmpdict

def menu():
    file = 'cook_book.txt'
    print("Сегодня в меню:")
    print(*filetodict(file, ' | '), sep=', ')
    print("Что будем готовить?")


menu()

with open('cook_book.txt', mode='r', encoding='UTF8') as fole:
    for line in fole:
        print(line, end='')
# t = get_shop_list_by_dishes(filetodict('cook_book.txt'), ['Запеченный картофель', 'Омлет'], 3)
#
# for m in t:
#     print(f"{m}: {t[m]}")
