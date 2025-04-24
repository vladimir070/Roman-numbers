arabic_numbers = list(range(1, 11))  # Пример: арабские числа от 1 до 10
roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]  # Соответствующие римские числа

while True:
    try:
        user_input = int(input("Введите арабское число (от 1 до 10, или 0 для выхода): "))

        if user_input == 0:
            break  # Выход из цикла

        if user_input in arabic_numbers:
            index = arabic_numbers.index(user_input)  # Находим индекс введенного числа
            roman_numeral = roman_numerals[index]  # Получаем римское число по индексу
            print(f"Римское число для {user_input}: {roman_numeral}")
        else:
            print("Введенное число не найдено в списке.")

    except ValueError:
        print("Пожалуйста, введите целое число.")