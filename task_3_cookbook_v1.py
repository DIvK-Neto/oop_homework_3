from pprint import pprint


# Функция по обработке текстового файла. Читаем файл и формируем построчный список
def file_processing():
    
    file = 'recipes.txt'
    
    with open(file, 'r', encoding='utf-8') as f:
        recipe_list = [line for line in f.read().split('\n')]  # формируем список из документа, для дальнейших действий с ним
    return recipe_list


# Функция по созданию кулинарного словаря из тектового файла
def list_processing(file_processing):
    
    cook_book = {}
    ingredients_dictionary = {}
    structure = ['ingredient_name', 'quantity', 'measure']
    temp_list = []
    complete_list = []
    
    for id, line in enumerate(file_processing):  # перебираем данные построчно
        if line:
            temp_list.append(line)  # наполняем строками временный лист
            if id+1 == len(file_processing):
                complete_list.append(temp_list)  # наполняем конечный список
        else:
            complete_list.append(temp_list)
            temp_list = []  # очищаем временный список

    for cook in complete_list:  # перебираем конечный список, отбираем имена блюд
        name = cook[0]
        cook_book[name] = []
        for el in cook[2:2+int(cook[1])]:  # перебираем ингредиенты
            ingredients_dictionary.update(dict(zip(structure, el.split(' | '))))  # наполняем словарь ингредиентами
            cook_book[name].append(ingredients_dictionary)  # собираем кулинарную книгу
            ingredients_dictionary = {}  # очищаем словарь ингредиентов

    return cook_book


# Функция для создания словаря с расчётом кол-ва ингридиентов на N персон
def get_shop_list_by_dishes(dishes, person_count):
    
    product_quantity = {}
    param_def = list_processing(file_processing())
    
    for dish in dishes:
        if param_def.get(dish):  # смотрим, есть ли блюдо в кулинарной книге
            for product in param_def.get(dish):  # перебираем ингредиенты и собираем новый словарь
                if not product_quantity.get(product['ingredient_name']):
                    product_quantity[product['ingredient_name']] = {
                        'measure': product['measure'],
                        'quantity': int(product['quantity']) * person_count
                    }
                else:
                    product_quantity[product['ingredient_name']
                                     ]['quantity'] += int(product['quantity']) * person_count

    return product_quantity


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
