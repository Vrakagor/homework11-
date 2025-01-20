def calculator():
    print("Модифікований калькулятор")

    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operation = input("Введіть дію (+, -, *, /): ").strip()

            if operation not in ['+', '-', '*', '/']:
                print("Невідома дія! Спробуйте ще раз.")
                continue

            num2 = float(input("Введіть друге число: "))

            if operation == '/' and num2 == 0:
                print("Помилка: ділити на нуль неможливо!")
                continue

            if operation == '+':
                print(f"Результат: {num1 + num2}")
            elif operation == '-':
                print(f"Результат: {num1 - num2}")
            elif operation == '*':
                print(f"Результат: {num1 * num2}")
            elif operation == '/':
                print(f"Результат: {num1 / num2}")

        except ValueError:
            print("Помилка! Введіть правильні числові значення.")
            continue

        again = input("Хочете продовжити? (y/n): ").strip().lower()
        if again != 'y':
            print("Дякую за використання калькулятора! До побачення!")
            break


if __name__ == "__main__":
    calculator()