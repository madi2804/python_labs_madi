import json

# Задание 1: Создание и использование словаря

menu = {
    "Американо": 3000,
    "Капучино": 3500,
    "Латте": 4500,
    "Моккачино": 3600
}

def get_price(drink_name):
    if drink_name in menu:
        print(f"Цена напитка {drink_name}: {menu[drink_name]} KRW")
    else:
        print("Такого напитка нет в меню")

# Задание 2: Изменение и удаление элементов словаря

menu["Флэт Уайт"] = 3800

if "Эспрессо" in menu:
    del menu["Эспрессо"]
else:
    print("Напиток 'Эспрессо' не найден в меню")

print("Итоговое меню кафе:")
for drink, price in menu.items():
    print(f"- {drink}: {price} KRW")

# Задание 3: Работа с JSON

book_info = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

json_data = json.dumps(book_info)
print("Строка JSON, представляющая информацию о книге:", json_data)

parsed_data = json.loads(json_data)
print("Словарь, полученный из строки JSON:", parsed_data)

# Решение Задания 4: Использование методов словаря


keys_list = list(menu.keys())
print("Список ключей:", keys_list)

values_list = list(menu.values())
print("Список значений:", values_list)

items_list = list(menu.items())
print("Список пар ключ-значение:", items_list)

# Задание 5: Словари и условные выражения

def drinks_below_price(menu, max_price):
    print(f"Напитки по цене ниже или равной {max_price} KRW:")
    for drink, price in menu.items():
        if price <= max_price:
            print(f"- {drink}: {price} KRW")

drinks_below_price(menu, 3600)
