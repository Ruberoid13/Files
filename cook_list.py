# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def file_to_dict(file, sep=' | '):
    counter = 0
    cook_book = dict()
    dish_name = str()
    with open(file, mode='r', encoding='UTF8') as opened_file:
        for line in opened_file:
            if line != '\n':
                if counter == 0:
                    dish_name = line.replace('\n', '')
                    cook_book.update({dish_name: []})
                if counter >= 2:
                    tmp_list = line.split(sep)
                    cook_book[dish_name].append({'ingredient_name': tmp_list[0],
                                                'quantity': int(tmp_list[1]), 'measure': tmp_list[2].replace('\n', '')})
            else:
                counter = -1
            counter += 1
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    tmp_list = []
    out_dict = {}
    for dish in cook_book:
        if dishes.count(dish) > 0:
            for engridient in cook_book[dish]:
                for tmp_engridient in tmp_list:
                    if tmp_engridient['ingredient_name'] == engridient['ingredient_name']:
                        tmp_list[tmp_list.index(tmp_engridient)]['quantity'] += engridient['quantity']
                        tmp_list[tmp_list.index(tmp_engridient)]['quantity'] *= person_count
                        break
                else:
                    engridient['quantity'] *= person_count
                    tmp_list.append(engridient)
    for engridient in tmp_list:
        engridient_name = engridient['ingredient_name']
        engridient.pop('ingredient_name')
        out_dict.update({engridient_name: engridient})
    return out_dict


def enumerate_menu(in_dict):
    counter = 1
    out_dict = {}
    for dish in in_dict:
        out_dict.update({counter: dish})
        counter += 1
    return out_dict


def print_numerated_dict(num_dict):
    for number in num_dict:
        print(f"{number}. {num_dict[number]}")


def make_list(in_dict):
    out_list = []
    input_num = -1
    print(f"Список блюд:")
    while len(in_dict) > 0 and input_num != 0:
        numerated_dict = enumerate_menu(in_dict)
        print_numerated_dict(numerated_dict)
        input_num = int(input(f"Выберите блюдо {1}{f' - {len(in_dict)}' if len(in_dict) > 1 else f''}."
                              f" Введите 0 для подсчета:\n"))
        if input_num in numerated_dict.keys():
            print(f"Добавили: '{list(in_dict.keys())[input_num - 1]}'.")
            out_list.append(list(in_dict.keys())[input_num - 1])
            in_dict.pop(list(in_dict.keys())[int(input_num) - 1])
            if len(in_dict) > 0:
                print(f'\nДобавить следующее блюдо?')
        elif input_num != 0:
            print("Неверный ввод!\n")
    return out_list


def menu():
    print("Создаем список покупок.\nВыберите блюда.")
    cook_book = file_to_dict('file.txt')
    inlist = make_list(file_to_dict('file.txt'))
    person_count = int(input("\nНа сколько персон готовить?\n"))
    engridient_list = get_shop_list_by_dishes(cook_book, inlist, person_count)
    print("\nСписок покупок:")
    counter = 1
    for engridient in engridient_list:
        print(f'{counter}. {engridient}: {engridient_list[engridient]["quantity"]} '
              f'{engridient_list[engridient]["measure"]}')
        counter += 1


menu()
