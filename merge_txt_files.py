def create_dict():
    file_name_list = ['1.txt', '2.txt', '3.txt']
    file_dict = {}
    for file in file_name_list:
        with open(file, mode='r', encoding='UTF-8') as f:
            file_dict.update({file: len(f.readlines())})
    return file_dict


def sort_dict(in_dict):
    sorted_dict = {}
    s_dict = sorted(in_dict.values())
    for j in range(len(in_dict)):
        for i in in_dict:
            if in_dict[i] == s_dict[j]:
                sorted_dict.update({i: in_dict[i]})
    return sorted_dict


def make_file(in_dict):
    with open('result.txt', mode='w', encoding='UTF-8') as new_file:
        for i in in_dict:
            with open(i, mode='r', encoding='UTF-8') as f:
                new_file.write(f'{i}\n{in_dict[i]}\n{f.read()}\n')


make_file(sort_dict(create_dict()))
