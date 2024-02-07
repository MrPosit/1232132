'''
Задание №1
Создайте класс Device, который содержит информацию об устройстве. С помощью 
механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о 
кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder 
(содержит информацию о мясорубке). Каждый из классов должен содержать необходимые 
для работы методы.
'''


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Бренд: {self.brand}, Модель: {self.model}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def brew_coffee(self):
        return "Заваривание кофе..."


class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def blend(self):
        return "Смешивание..."


class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        return "Измельчение мяса..."


'''
Задание №2
Создайте класс Ship, который содержит информацию о корабле. С помощью механизма 
наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer 
(содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере). 
Каждый из классов должен содержать необходимые для работы методы.
'''


class Ship:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_info(self):
        return f"Имя: {self.name}, Год: {self.year}"


class Frigate(Ship):
    def __init__(self, name, year, weapons):
        super().__init__(name, year)
        self.weapons = weapons

    def fire_weapon(self):
        return "Огнестрельное оружие..."


class Destroyer(Ship):
    def __init__(self, name, year, missiles):
        super().__init__(name, year)
        self.missiles = missiles

    def launch_missile(self):
        return "Запуск ракеты..."


class Cruiser(Ship):
    def __init__(self, name, year, size):
        super().__init__(name, year)
        self.size = size

    def maneuver(self):
        return "Выполнение маневра..."


'''
Задание №1
Используя понятие множественного наследования, разработайте класс «Окружность, 
вписанная в квадрат».
'''


class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def area(self):
        return self.side ** 2


class CircleInSquare(Square):
    def __init__(self, x, y, side):
        super().__init__(x, y, side)

    def radius(self):
        return self.side / 2

    def area(self):
        return 3.14 * (self.side / 2) ** 2


'''
Задание №2
Используя механизм множественного наследования разработайте класс “Автомобиль”. 
Должны быть классы «Колеса», «Двигатель», «Двери»
'''


class Wheels:
    def __init__(self, size):
        self.size = size

    def rotate(self):
        return "Колеса вращающиеся..."


class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return "Запуск двигателя..."


class Doors:
    def __init__(self, number):
        self.number = number

    def open(self):
        return "Двери открываются..."


class Car(Wheels, Engine, Doors):
    def __init__(self, size, power, number):
        Wheels.__init__(self, size)
        Engine.__init__(self, power)
        Doors.__init__(self, number)


'''
Задание №3
Создайте базовый класс Shape для рисования плоских фигур. 
Определите методы: 
Show() — вывод на экран информации о фигуре; 
Save() — сохранение фигуры в файл; 
Load() — считывание фигуры из файла. 
Определите производные классы: 
Square — квадрат, который характеризуется координатами левого верхнего угла и 
длиной стороны; 
Rectangle — прямоугольник с заданными координатами верхнего левого угла и 
размерами; 
2
Circle — окружность с заданными координатами центра и радиусом; 
Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него 
прямоугольника со сторонами, параллельными осям координат, и размерами этого 
прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список 
и отобразите информацию о каждой из фигур
'''


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        pass

    def save(self):
        pass

    def load(self):
        pass


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def show(self):
        print(f"Квадрат: x={self.x}, y={self.y}, сторона={self.side}")

    def save(self):
        with open("square.txt", "w") as file:
            file.write(f"{self.x},{self.y},{self.side}")

    def load(self):
        with open("square.txt", "r") as file:
            data = file.readline().split(",")
            self.x = int(data[0])
            self.y = int(data[1])
            self.side = int(data[2])


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        print(f"Круг: x={self.x}, y={self.y}, радиус={self.radius}")

    def save(self):
        with open("circle.txt", "w") as file:
            file.write(f"{self.x},{self.y},{self.radius}")

    def load(self):
        with open("circle.txt", "r") as file:
            data = file.readline().split(",")
            self.x = int(data[0])
            self.y = int(data[1])
            self.radius = int(data[2])


shapes = [Square(0, 0, 5), Circle(2, 3, 7)]
for shape in shapes:
    shape.show()
    shape.save()

new_shapes = []
for shape in shapes:
    if isinstance(shape, Square):
        new_shape = Square(0, 0, 0)
    elif isinstance(shape, Circle):
        new_shape = Circle(0, 0, 0)
    new_shape.load()
    new_shapes.append(new_shape)

for shape in new_shapes:
    shape.show()
