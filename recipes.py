def cook_book(file_name):

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


def get_shop_list_by_dishes(dishes, person_count):
    book = cook_book('recipes.txt')
    ingridients = []
    for key in book:
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
    while index_1 < len(food_list):
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

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
