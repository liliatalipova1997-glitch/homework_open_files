def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:

        return f.read()

def get_data_list(text):
    list = []
    for i in text.split('\n\n'):
        list.append(i.splitlines())

    return list

def clean_data_list(list):
    b = []
    for list_data in list:
        a = []
        a += list_data[:1]
        for i in list_data[2:]:
            a.append(i.split(' | '))
        b.append(a)

    return b

def get_cookbook_dict(list):
    a = {}
    for i in list:
        a[i[0]] = []
        for j in i[1:]:
            a[i[0]].append({'ingredient_name': j[0], 'quantity': int(j[1]), 'measure': j[2]})

    return a

def make_cookbook_dict_from_text(file_path):
    text = read_file(file_path)
    dish_list = get_data_list(text)
    cleaned_dish_list = clean_data_list(dish_list)

    return get_cookbook_dict(cleaned_dish_list)
 

cook_book = make_cookbook_dict_from_text('recipes.txt')
# print(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        for j in cook_book[i]:
            new_shop_list= dict(j)
            new_shop_list['quantity'] *= person_count
            if new_shop_list['ingredient_name'] not in shop_list:
                shop_list[new_shop_list['ingredient_name']] = {'measure': new_shop_list['measure'], 'quantity': new_shop_list['quantity']}
            else:
                shop_list[new_shop_list['ingredient_name']]['quantity'] += new_shop_list['quantity']

    return shop_list


ingredients_dict = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1)
# print(ingredients_dict)


# def read_files(path1=None, path2=None, path3=None):
#     with open(path1, 'r', encoding='utf-8') as f:
#         txt_1 = f.read()
#     list_1 = []
#     for i in txt_1.split('\n'):
#         list_1.append(i.splitlines())

#     with open(path2, 'r', encoding='utf-8') as f:
#         txt_2 = f.read()
#     list_2 = []
#     for i in txt_2.split('\n'):
#         list_2.append(i.splitlines())

#     with open(path3, 'r', encoding='utf-8') as f:
#         txt_3 = f.read()
#     list_3 = []
#     for i in txt_3.split('\n'):
#         list_3.append(i.splitlines())

#     all_list = [list_1,  list_2,  list_3]
#     all_list.sort(reverse=True)
#     for i in all_list:
#         n = 0
#         print(i)
#         print(len(i))
#         for j in i:
#             n += 1
#             print(f'Строка номер {n} файла номер {len(i)}')

#             # print(f'1.txt, {a}{len(list_1)}')
#     #     for i in range(len(list_1)):
#     #         print(f'Строка номер {i+1} файла номер 2')






# dd = read_files('1.txt','2.txt','3.txt')








def read_files(path1=None, path2=None, path3=None):
    with open(path1, 'r', encoding='utf-8') as f:
        txt_1 = f.read()

    lines_1 = txt_1.split('\n')
    list_1 = [path1, len(lines_1), 1]
    list_1 += lines_1
    
    # for i in txt_1.split('\n'):
    #     list_1.append(i.splitlines())

    with open(path2, 'r', encoding='utf-8') as f:
        txt_2 = f.read()
    
    lines_2 = txt_2.split('\n')
    list_2 = [path2, len(lines_2), 2]
    list_2 += lines_2
    with open(path3, 'r', encoding='utf-8') as f:
        txt_3 = f.read()
    lines_3 = txt_3.split('\n')
    list_3 = [path3, len(lines_3), 3]
    list_3 += lines_3
    all_list = [list_1, list_2, list_3]
    all_list.sort(key=len)

    i = 1
    for file in all_list:
        
        print(file[0],file[1], sep = '\n')
        lines_number = file[1]
        for n in range(lines_number):
            n += 1
            print(f'Строка номер {n} файла номер {file[2]}')
        
        i += 1


dd = read_files('1.txt','2.txt','3.txt')