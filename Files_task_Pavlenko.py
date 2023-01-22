
def print_cook_book(cook_book):
    print('cook_book = {')
    number_of_recepies = len(cook_book)
    n=0
    for dish in cook_book:
        print(f"  '{dish}': [")
        for i in range(len(cook_book[dish])):
            print(f'     {cook_book[dish][i]}')
        n += 1
        if n < number_of_recepies:
            print('     ],')
        else:
            print('     ]')
    print('}')

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list= {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] not in shop_list:
                shop_list[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': person_count*ingridient['quantity']}
            else:
                shop_list[ingridient['ingredient_name']]['quantity'] += person_count*ingridient['quantity']
    print('{')
    number_of_ingridients = len(shop_list)
    n=1
    for ingridient in shop_list:
        if n < number_of_ingridients:
            print(f"    '{ingridient}': {shop_list[ingridient]},")
        else:
            print(f"    '{ingridient}': {shop_list[ingridient]}")
        n += 1
    print('}')


with open ('recepies.txt', 'r', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingridients_number = int(file.readline().strip())
        dish_ingridients = []
        for i in range(ingridients_number):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dish_ingridients.append ({'ingredient_name': ingredient_name,'quantity': int(quantity),'measure': measure})
        cook_book[dish_name] = dish_ingridients
        file.readline()

print_cook_book(cook_book)
print()
get_shop_list_by_dishes(cook_book, ['Фахитос', 'Омлет'], 2)
