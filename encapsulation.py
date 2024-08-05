class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, num1, num2):
        self.__result = num1 + num2
        return self.__result

    def subtract(self, num1, num2):
        self.__result = num1 - num2
        return self.__result

    def get_result(self):
        return self.__result

calc = Calculator()

addition_result = calc.add(10, 5)
print(f"Addition Result: {addition_result}")

subtraction_result = calc.subtract(10, 5)
print(f"Subtraction Result: {subtraction_result}")

final_result = calc.get_result()
print(f"Final Result stored in Calculator: {final_result}")