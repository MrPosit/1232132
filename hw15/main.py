'''Напишите программу, в которой есть главный класс с текстовым полем. В главное 
классе должен быть метод для присваивания значения полю: без аргументов и с одним 
текстовым аргументом. Объект главного класса создаётся передачей одного текстового 
аргумента конструктору. На основе главного класса создается класса потомок. 
В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента'''

class MainClass:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number


main_obj = MainClass("Hello")
main_obj.set_text("World")
print(main_obj.get_text())

sub_obj = SubClass("Hi", 42)
print(sub_obj.get_text())
print(sub_obj.get_number())



