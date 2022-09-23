# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def file_to_dict(file, sep=' | '):
    c = 0
    cook_book = dict()
    dishname = str()
    with open(file, mode='r', encoding='UTF8') as f:
        for line in f:
            if line != '\n':
                if c == 0:
                    dishname = line.replace('\n', '')
                    cook_book.update({dishname: []})
                if c >= 2:
                    tmplist = line.split(sep)
                    cook_book[dishname].append({'ingredient_name': tmplist[0], 'quantity': tmplist[1], 'measure': tmplist[2]})
            else:
                c = -1
            c += 1
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


def enumerate_menu(in_dict):
    c = 1
    out_dict = {}
    for i in in_dict:
        out_dict.update({c: i})
        c += 1
    return out_dict

# def enumerate_menu(in_dict):
#     c = 1
#     out_dict = {}
#     for i in in_dict:
#         out_dict.update({c: {i: in_dict[i]}})
#         c += 1
#     return out_dict


def menu():
    file = 'file.txt'
    menu = file_to_dict(file)
    menu_numbers = enumerate_menu(menu)
    print("Сегодня в меню:")
    for i in menu_numbers:
        print(f"{i}. {menu_numbers[i]}")

    print("\nЧто будем готовить?")
    n = int(input(f"Введите число от 1 до {len(menu_numbers)} или '0' для выхода:"))
    while n not in menu_numbers and n != 0:
        n = int(input(f"Введите число от 1 до {len(menu_numbers)} или 0 для выхода:"))
    if n == 0:
        print("Выход из программы...")
        return
    # menu_numbers[n]

    print(f"Готовим: {menu_numbers[n]}")
    c = int(input(f"Сколько персон ожидается? Введите число от 1 до дофига или 0 для выхода:"))
    while c < 0 and c != 0:
        c = int(input(f"Введите число от 1 до дофига или 0 для выхода:"))
    if c == 0:
        print("Выход из программы...")
        return



menu()
# enumerate_menu(file_to_dict('file.txt'))
