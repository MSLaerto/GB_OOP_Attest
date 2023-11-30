import logging
from abc import ABC, abstractmethod
# Интерфейс операции
class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Конкретные операции
class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

class Division(Operation):
    def execute(self, a, b):
        if b != 0:
            return a / b
        else:
            logging.error("Деление на ноль!")

class CalculatorView:
    def __init__(self):
        self.calculator = None

    def show_menu(self):
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Умножение")
        print("3. Деление")
        print("0. Выход")

    def get_operation_choice(self):
        choice = input("Введите номер операции: ")
        if choice.isdigit():
            return int(choice)
        else:
            print("Некорректный ввод. Повторите попытку.")
            return self.get_operation_choice()

    def get_numbers(self):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        return a, b

    def show_result(self, result):
        print(f"Результат: {result}")

    def show_error(self, error_message):
        print(f"Ошибка: {error_message}")

    def run(self):
        while True:
            self.show_menu()
            operation_choice = self.get_operation_choice()
            if operation_choice == 1:
                self.calculator = Calculator(Addition())
            elif operation_choice == 2:
                self.calculator = Calculator(Multiplication())
            elif operation_choice == 3:
                self.calculator = Calculator(Division())
            elif operation_choice == 0:
                return 0     
            else:
                self.show_error("Некорректный выбор операции.")
            a, b = self.get_numbers()
            result = self.calculator.calculate(a, b)
            self.show_result(result)
class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, a, b):
        result = self.operation.execute(a, b)
        logging.info(f"Результат: {result}")
        return result