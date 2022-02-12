def cook_book(file_name): # Задание 1
    dishes = []
    dish = []
    ingredients = []
    recipes = {}
    cook = {}
    book = []
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dishes.append(line.strip())
            dish_quantity = int(file.readline().strip())
            for ing in range(dish_quantity):
                file.readline()
            file.readline() * 5
    index_1 = 0
    index_2 = 0
    index_3 = 0
    index_4 = 0
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish.append(line.strip())
    while index_1 < len(dish):
        if dish[index_1] == dishes[index_2]:
            index_1 += 1
            dish_quantity = int(dish[index_1])
            while index_3 < dish_quantity:
                index_1 += 1
                ingredients.append(list(dish[index_1].split(' | ')))
                ingridient = ''
                cook['ingredient_name'] = ingredients[index_3][index_4]
                index_4 += 1
                cook['quantity'] = ingredients[index_3][index_4]
                index_4 += 1
                cook['measure'] = ingredients[index_3][index_4]
                index_4 = 0
                book.append(cook)
                cook = {}
                index_3 += 1
            index_3 = 0
            recipes[dishes[index_2]] = book
            index_2 += 1
            ingredients = []
        book = []
        index_1 += 1
    res = recipes
    return res


def get_shop_list_by_dishes(dishes, person_count): # Задание 2
    book = cook_book('recipes.txt')
    ingridients = []
    for key in book: # Достаём список продуктов из словаря
        for dish in dishes:
            if key == dish:
                ingridients.append(book[key])
    food_list = []
    for recipe in ingridients:
        for food in recipe:
            food_list.append(list(food.values()))
    index_1 = 0
    index_2 = 1
    food = {}
    count = {}
    while index_1 < len(food_list): # Перебираем продукты и создаём список согласно условиям задания
        while index_2 < len(food_list):
            if food_list[index_1][0] == food_list[index_2][0]:
                food_list[index_1][1] = int(food_list[index_1][1]) * 2
                del(food_list[index_2])
            index_2 += 1
        food_list[index_1][1] = int(food_list[index_1][1]) * int(person_count)
        count['measure'] = food_list[index_1][2]
        count['quantity'] = food_list[index_1][1]
        food[food_list[index_1][0]] = count
        count = {}
        index_1 += 1
        index_2 = index_1 + 1
    return food


def length_lines(): # Задание 3
    with open('total.txt', 'w', encoding='utf-8'): # Добавил для того, чтобы файл очищался при каждом запуске функции
        pass
    file_1 = []
    file_2 = []
    file_3 = []
    with open('1.txt', encoding='utf-8') as file:
        for line in file:
            file_1.append(line.strip())
    with open('2.txt', encoding='utf-8') as file:
        for line in file:
            file_2.append(line.strip())
    with open('3.txt', encoding='utf-8') as file:
        for line in file:
            file_3.append(line.strip())
    with open('total.txt', 'a', encoding='utf-8') as file:
        if len(file_1) < len(file_2) < len(file_3):
            file.write('1.txt' + '\n')
            file.write(str(len(file_1)) + '\n')
            for line in file_1:
                file.write(line + '\n')
            if len(file_2) < len(file_3):
                file.write('2.txt' + '\n')
                file.write(str(len(file_2)) + '\n')
                for line in file_2:
                    file.write(line + '\n')
                file.write('3.txt' + '\n')
                file.write(str(len(file_3)) + '\n')
                for line in file_3:
                    file.write(line + '\n')
            else:
                file.write('3.txt' + '\n')
                file.write(str(len(file_3)) + '\n')
                for line in file_3:
                    file.write(line + '\n')
                file.write('2.txt' + '\n')
                file.write(str(len(file_2)) + '\n')
                for line in file_2:
                    file.write(line + '\n')

        elif len(file_1) > len(file_2) < len(file_3):
            file.write('2.txt' + '\n')
            file.write(str(len(file_2)) + '\n')
            for line in file_2:
                file.write(line + '\n')
            if len(file_1) < len(file_3):
                file.write('1.txt' + '\n')
                file.write(str(len(file_1)) + '\n')
                for line in file_1:
                    file.write(line + '\n')
                file.write('3.txt' + '\n')
                file.write(str(len(file_3)) + '\n')
                for line in file_3:
                    file.write(line + '\n')
            else:
                file.write('3.txt' + '\n')
                file.write(str(len(file_3)) + '\n')
                for line in file_3:
                    file.write(line + '\n')
                file.write('1.txt' + '\n')
                file.write(str(len(file_1)) + '\n')
                for line in file_1:
                    file.write(line + '\n')
        else:
            file.write('3.txt' + '\n')
            file.write(str(len(file_3)) + '\n')
            for line in file_3:
                file.write(line + '\n')
            if len(file_1) < len(file_2):
                file.write('1.txt' + '\n')
                file.write(str(len(file_1)) + '\n')
                for line in file_1:
                    file.write(line + '\n')
                file.write('2.txt' + '\n')
                file.write(str(len(file_2)) + '\n')
                for line in file_2:
                    file.write(line + '\n')
            else:
                file.write('2.txt' + '\n')
                file.write(str(len(file_2)) + '\n')
                for line in file_2:
                    file.write(line + '\n')
                file.write('1.txt' + '\n')
                file.write(str(len(file_1)) + '\n')
                for line in file_1:
                    file.write(line + '\n')