from pprint import pprint
def book(encoding):
    with open('recipes.txt', encoding=encoding) as file:
        cook_book = {}
        for dish in file:
            num_of_ingredients = int(file.readline())
            list_of_ingredients = []
            for item in range(num_of_ingredients):
                compare = file.readline().split(' | ')
                dict_ingredients = ({'name': compare[0], 'number': compare[1], 'measure': compare[2].strip('\n')})
                list_of_ingredients.append(dict_ingredients)
            cook_book[dish.strip('\n')] = list_of_ingredients
            file.readline()

    return cook_book

pprint(book('utf-8'))


def get_shop_list_by_dishes(dishes, person_count):

    cook_book = book('utf-8')
    ingredients_dishes = {}

    for dish in dishes:    # Прохожусь по списку блюд
        if dish in cook_book:   # Проверяю, есть ли блюдо в словаре
            for item in cook_book[dish]:   # Прохожу циклом по значению блюда
                if 'name' in item:  # Проверяю наличие ключа в значении блюда
                    ingredients_dishes[item['name']] = {int(item['number']) * person_count, item['measure']}

    return ingredients_dishes

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))