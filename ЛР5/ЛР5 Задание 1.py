# Определение класса C
class C:
    def __init__(self, a, b=5): # Инициализатор класса, принимает параметры a и b (по умолчанию b=5)
        # Присваиваем значения параметров a и b атрибутам объекта
        self.a = a
        self.b = b

    # Метод c возвращает сумму значений a и b объекта
    def c(self):
        return self.a + self.b

    # Метод d возвращает разность значений a и b объекта
    def d(self):
        return self.a - self.b


a1 = C(5)# Создаем объект класса C с параметром a=5 (b принимает значение по умолчанию, то есть 5)
print(f'{a1.a}+{a1.b}=', a1.c())# Выводим результат сложения a и b объекта a1
a2 = C(4, 6)# Создаем объект класса C с параметрами a=4 и b=6
print(f'{a2.a}-{a2.b}=', a2.d()) # Выводим результат вычитания b из a объекта a2
