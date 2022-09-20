# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def filetodict(file, sep='|'):
    tmplist = list()
    cook_book = {}
    tmpdict = {}
    tl3 = list()
    f = open(file, mode='r', encoding='utf-8')

    for line in f:
        if line != '\n':
            tmplist.append(line.replace('\n', ''))
        else:
            for i in range(2, len(tmplist)):
                tl2 = tmplist[i].split(sep)
                tl3.append({'ingredient_name': tl2[0], 'quantity': tl2[1], 'measure': tl2[2]})
            cook_book.update({tmplist[0]: tl3})
            tmplist = list()
            tl3 = list()
    for i in cook_book:
        print(i)
        for j in cook_book[i]:
            print(f"  {j}")
        pass
    # print(cook_book)

filetodict('files.txt')
