# import chardet

def get_menu(fname) :
    cook_book = {}
    with open(fname) as f:
        for line in f:
            str = line.strip()
            if str.isalpha():
                dish = str
                cook_book[dish] = []
            elif str.isdigit(): continue
            else:
                ingrid = str.strip().split(' | ')
                cook_book[dish].append({'ingridient_name': ingrid[0], 'quantity': int(ingrid[1]), 'measure': ingrid[2]})
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    cook_book = get_menu('dishes.txt')
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)




create_shop_list()


