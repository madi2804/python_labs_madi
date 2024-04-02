print("Задание 1:")
for i in range(1, 21):
    print(i)

print("\nЗадание 2:")
numbers = list(range(1, 11))
for number in numbers:
    print(number ** 2)

print("\nЗадание 3:")
breads = ["хлеб1", "хлеб2", "хлеб3"]
meats = ["мясо1", "мясо2", "мясо3"]
vegetables = ["овощи1", "овощи2", "овощи3"]
sauces = ["соус1", "соус2", "соус3"]

sandwiches = [(bread, meat, vegetable, sauce) for bread in breads for meat in meats for vegetable in vegetables for sauce in sauces]
for sandwich in sandwiches:
    print(sandwich)

print("\nЗадание 4:")
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Сумма четных чисел:", even_sum)
print("Сумма нечетных чисел:", odd_sum)

print("\nЗадание 5:")
num = int(input("Введите число для вычисления факториала: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Факториал числа", num, "равен", factorial)

print("\nЗадание 6:")
persons = [["Иван", 25, "М", 180, 75], ["Мария", 30, "Ж", 165, 60], ["Петр", 40, "М", 175, 80]]

total_age = sum(person[1] for person in persons)
average_age = total_age / len(persons)
print("Средний возраст всех персон в списке:", average_age)

print("\nЗадание 7:")
numbers = list(range(1, 11))
print(numbers[2:7])

print("\nЗадание 8:")
fruits = ["яблоко", "банан", "апельсин"]
if "яблоко" in fruits:
    print("Список содержит яблоко.")

print("\nЗадание 9:")
my_tuple = (10, "строка", [1, 2, 3])
print("Кортеж целиком:", my_tuple)
print("Элементы кортежа:")
for item in my_tuple:
    print(item)

print("\nЗадание 10:")
numbers = list(range(1, 6))
numbers.append(6)
numbers.remove(3)
numbers.sort(reverse=True)
print(numbers)
