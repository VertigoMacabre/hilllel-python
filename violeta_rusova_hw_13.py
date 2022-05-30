from abc import abstractmethod

"""Сделать примеры в файлике.
__call__
__repr__
@classmethod &@staticmethod
@property, setter, deleter"""


# __call__ метод дозволяє писати класи, де екземпляри поводяться як функції і можуть бути викликані як функція
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("An argument should be a string")

        return args[0].replace(self.__chars, "\n")


# __repr__ — це спеціальний метод, який використовується для представлення об'єктів класу у вигляді рядка


class GreatBritainBands:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The band {self.name} is an English band"


# @classmethod, @staticmethod, @property, @setter, @deleter + @abstractmethod бонусом

class Animal:
    _name: str
    age: int
    favorite_food_name: str
    COUNT: int = 0

    @abstractmethod
    def make_a_sound(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    def class_name():
        return __class__.__name__

    def __init__(self, name: str, age: int):
        Animal.COUNT = Animal.COUNT + 1
        self.age = age
        self.__name = name

    @classmethod
    def count_of_animals(cls):
        return cls.COUNT

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name


class Cat(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._favorite_food_name = "fish"

    def make_a_sound(self):
        return "Meow!"

    def __str__(self):
        return f"Name is {self.name}, {self.age} year old, likes to eat {self._favorite_food_name} " \
               f"it makes sound - {self.make_a_sound()}"

    @staticmethod
    def class_name():
        return __class__.__name__


if __name__ == '__main__':
    # __call__
    string_1 = StripChars(", ")
    str_result = string_1("He was turned to steel, In the great magnetic field, When he traveled time, For the future "
                          "of mankind")
    print(str_result)

    # __repr__
    my_band = GreatBritainBands("Black Sabbath")
    print(my_band)

    # @classmethod, @staticmethod, @property, @setter, @deleter + @abstractmethod бонусом
    loki: Animal = Cat("Loki", 4)
    print(loki) # abstract method
    print(Cat.class_name())  # static method
    print(Cat.count_of_animals())  # class method

    loki.name = "Odin"  # міняємо приватне ім'я
    print(loki.name)  # приватне ім'я змінено

    del loki.name  # видаляємо приватне ім'я

    print(vars(loki))  # перевіряємо, що приватне ім'я зникло
