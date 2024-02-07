'''Задание №1'''
'''
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, 
год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса 
для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''
class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель: ")
        self.year = input("Год: ")
        self.manufacturer = input("Производитель: ")
        self.engine_volume = input("Обьем двигателя: ")
        self.color = input("Цвет: ")
        self.price = input("Цена: ")

    def output_data(self):
        print("Модель:", self.model)
        print("Год:", self.year)
        print("Производитель:", self.manufacturer)
        print("Обьем двигателя:", self.engine_volume)
        print("Цвет:", self.color)
        print("Цена:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


car1 = Car("", "", "", "", "", "")
car1.input_data()
car1.output_data()


'''Задание №2'''
'''
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год 
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода 
данных, реализуйте доступ к отдельным полям через методы класса.
'''
class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Название: ")
        self.year = input("Год: ")
        self.publisher = input("Издатель: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = input("Цена: ")

    def output_data(self):
        print("Название:", self.title)
        print("Год:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


book1 = Book("", "", "", "", "", "")
book1.input_data()
book1.output_data()


'''Задание №3'''
'''
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, 
дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных, 
вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Название стадиона: ")
        self.opening_date = input("Дата открытия: ")
        self.country = input("Страна: ")
        self.city = input("Город: ")
        self.capacity = input("Емкость: ")

    def output_data(self):
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Емкость:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity


stadium1 = Stadium("", "", "", "", "")
stadium1.input_data()
stadium1.output_data()


'''ООП. Инкапсуляция'''
'''
Напишите программу, в которой есть главный класс с текстовым полем. В главное классе 
должен быть метод для присваивания значения полю: без аргументов и с одним текстовым 
аргументом. Объект главного класса создаётся передачей одного текстового аргумента 
конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно 
добавить числовое поле. У конструктора класса-потомка два аргумента.
'''
class ParentClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        self.text = text

    def print_text(self):
        print("Text:", self.text)


class ChildClass(ParentClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number

    def print_number(self):
        print("Number:", self.number)


child_obj = ChildClass("Hello", 10)
child_obj.print_text()
child_obj.print_number()
