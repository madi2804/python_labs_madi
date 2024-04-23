# Задание 1: Шифр Цезаря

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# Задание 2: Работа с глобальными и локальными переменными

global_var = 10  

def demonstrate_variables():
    local_var = 20 
    print("Локальная переменная local_var:", local_var)
    print("Глобальная переменная global_var:", global_var)

# Задание 3: Использование параметров по умолчанию и ключевых параметров

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Задание 4: Возврат нескольких значений из функции

def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Задание 5: Форматирование строк

name = "Alice"
age = 30


encrypted_text = caesar_cipher("Hello, World!", 3)
print("Зашифрованный текст:", encrypted_text)

demonstrate_variables()

greet("Alice") 
greet("Bob", "Hi")  

numbers_list = [5, 8, 2, 10, 6]
min_value, max_value, average = calculate_stats(numbers_list)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", average)


formatted_str = "Name: {}, Age: {}".format(name, age)
print(formatted_str)

formatted_str = "Name: {0}, Age: {1}".format(name, age)
print(formatted_str)

formatted_str = "Name: {name}, Age: {age}".format(name=name, age=age)
print(formatted_str)
