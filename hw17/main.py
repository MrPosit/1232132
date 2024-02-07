'''
Задание №1
Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных 
операторов:
Проверка на равенство радиусов двух окружностей (операция = =);
Сравнения длин двух окружностей (операции >, <, <=,>=);
Пропорциональное изменение размеров окружности, путем изменения ее радиуса 
(операции + - += -=)
'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self


'''
Задание №2
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации арифметических операций для по 
работе с комплексными числами (операции +, -, *, /).
'''


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real + 2 ** other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)


'''
Задание №3
Вам необходимо создать класс Airplane (самолет). 
С помощью перегрузки операторов реализовать: 
Проверка на равенство типов самолетов (операция = =); 
Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
Сравнение двух самолетов по максимально возможному количеству пассажиров на 
борту (операции > < <= >=).
'''


class Airplane:
    def __init__(self, model, max_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.passengers = 0

    def __eq__(self, other):
        return self.model == other.model

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, passengers):
        self.passengers += passengers
        return self

    def __sub__(self, passengers):
        self.passengers -= passengers
        return self

    def __iadd__(self, passengers):
        self.passengers += passengers
        return self

    def __isub__(self, passengers):
        self.passengers -= passengers
        return self


'''
Задание №4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
Проверка на равенство площадей квартир (операция ==);
Проверка на неравенство площадей квартир (операция !=);
Сравнение двух квартир по цене (операции > < <= >=).
'''


class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


'''
Создайте класс Roman (РимскоеЧисло), представляющий римское число и 
поддерживающий операции +, -, *, /.
При реализации класса:
операции +, -, *, / реализуйте как специальные методы 
методы преобразования как статические методы
'''


class Roman:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        return Roman(self.value / other.value)

    @staticmethod
    def to_roman(number):
        pass

    @staticmethod
    def from_roman(roman):
        pass
