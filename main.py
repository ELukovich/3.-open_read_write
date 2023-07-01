

cook_book = {}

with open('recipes.txt', encoding = "utf-8") as f:
    for line in f:
        ingredient_list = []
        menu = {}
        dish_name = line.strip()
        ingredient_quantity = f.readline()
        for ingredient_all in range(int(ingredient_quantity)):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredient_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        dish = {dish_name: ingredient_list}
        emp = f.readline()
        cook_book.update(dish)




    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if dish in cook_book:
                for product in cook_book[dish]:
                    if product['ingredient_name'] in shop_list:
                        shop_list[product['ingredient_name']]['quantity'] += int(product['quantity']) * person_count
                    else:
                        shop_list[product['ingredient_name']] = {'measure': product['measure'], 'quantity': (int(product['quantity']) * person_count)}
            else:
                print('Такого блюда нет в книге')

        print(f'Список покупок: \n{shop_list}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print()
print(f'cook_book = {cook_book}')


# Задача 3
