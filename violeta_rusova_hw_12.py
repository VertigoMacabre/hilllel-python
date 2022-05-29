from functools import reduce
from abc import abstractmethod


# ЗАДАЧА 1: написать 3 примера генераторных функций с различными последовательностями.
def task_1_factorial(n: int):
    product_of_numbers = 1
    for i in range(1, n + 1):
        product_of_numbers *= i
        yield product_of_numbers


def task_1_string_words_first_letter_upper(input_string: str):
    splited_string = input_string.split(" ")

    for word in splited_string:
        capitalized_word = word.capitalize()
        yield capitalized_word


def task_1_get_diff_between_by_fields(list_of_objects: list, field: str):
    diff: dict = {field: 0, 'month': None}
    previous_object: dict = {field: 0, "month": None}

    for object in list_of_objects:
        diff[field] = object[field] - previous_object[field]
        diff["month"] = object["month"]
        previous_object = object
        yield diff

    # ЗАДАЧА 2: написать свою реализацию функции reduce() с описанием в инлайновых и многострочных комментариях ее работы.
    """Функція reduce приймає функцію та послідовність, застосовує цю функцію до елементів послідовності
    та повертає ОДНЕ значення"""


# результат буде залежати від анонімної функції, тайп хінт object не ставимо
def task2_our_own_reduce(func, sequence, by_field=None):
    try:
        # Створюємо ітератор
        sequence_iterator = iter(sequence)

        # Якщо в нас є by_field, ми розуміємо, що це послідовність об'єктів
        if bool(by_field):
            """Так як наша лямбда функція func працює с числами, а не об'єктами,
            ми беремо значення поля об'єкта.
            Опрацьовуємо первую ітерацію, так як наша лямбда функція func приймає 2 числа,
            а на першому кроку в нас тільки одне (немає  "попереднього" числа)
            Відбувається ітерація при індексі 0"""
            accumulated = next(sequence_iterator)[by_field]
        else:
            """
            Якщо ми не передаємо by_field, розуміємо, що проста послідовність, наприклад чисел.
            Опрацьовуємо першу ітерацію, так як наша лямбда функція func приймає 2 числа,
            а на першому кроку в нас тільки одне (немає  "попереднього" числа)
            Відбувається ітерація при індексі 0
            """
            accumulated = next(sequence_iterator)

        """
        На цьому етапі наш ітератор починає проход вже з індексу 1,
        й ми маємо результат виконання функції func на попередньому кроці (індекс 0)
        """
        for o in sequence_iterator:
            if bool(by_field):
                """
                Так как наша анонімная функція func працює с числами, а не об'єктами,
                ми беремо значення поля об'єкта, у данному випадку - число.
                В accumulated теж число.
                Передаємо їх в лямбда функцію func
                """

                accumulated = func(accumulated, o[by_field])

            else:
                """
                Якщо ми не передаємо by_field, розуміємо,що це проста послідовність, наприклад, числа.
                Опрацьовуємо першу ітерацію, так як наша лямбда функція func приймає 2 числа.
                "o" в даному вмпадку - число
                В accumulated - теж число
                """

                accumulated = func(accumulated, o)

        # повертаємо акумульований результат
        return accumulated

    except TypeError:
        print("Objects are not iterable")  # реалізуємо exception на випадок, якщо у нас неітерабельний тип даних


def task3_reduce_result_check_test(expected, actual):
    try:
        assert expected == actual
    except AssertionError:
        print(f"Expected value {expected} is not equal to actual value {actual}")


#
#

class Animal:
    name: str
    age: int
    favorite_food_name: str

    @abstractmethod
    def make_a_sound(self):
        pass

    def inspect(self):
        print(dir(self))


class Cat(Animal):

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
        self.favorite_food_name = "fish"

    def make_a_sound(self):
        return "Meow!"


class Dog(Animal):

    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
        self.favorite_food_name = "meat"

    def make_a_sound(self):
        return "Bark!"


if __name__ == '__main__':

    # Задача 1

    factorials = task_1_factorial(5)

    for factorial in factorials:
        print(factorial)

    first_to_upper = task_1_string_words_first_letter_upper("hello, world")
    for word in first_to_upper:
        print(word)

    objects_list = [
        {
            "month": 1,
            "sales": 15,
            "profit": 100,
        },
        {
            "month": 2,
            "sales": 40,
            "profit": 90,
        },
        {
            "month": 3,
            "sales": 25,
            "profit": 230,
        }
    ]

    for diff in task_1_get_diff_between_by_fields(objects_list, "sales"):
        print(diff)

    for diff in task_1_get_diff_between_by_fields(objects_list, "profit"):
        print(diff)

    # Задача 2-3

    # Результат виконання нашого reduce з послідовністю словників
    result = task2_our_own_reduce(lambda a, b: a * b, objects_list, by_field="sales")
    print("My reduce result is", result)

    # Тест assert, який повинен пройти
    task3_reduce_result_check_test(15 * 40 * 25, result)
    # Тест assert, який НЕ повинен пройти - визове виключення
    task3_reduce_result_check_test(15 * 40 * 25 * 3, result)

    # Результат виконання нашого reduce з послідовністю з чисел
    result = task2_our_own_reduce(lambda a, b: a - b, [1, 2, 3])
    print("My reduce result is", result)
    # Тест assert, який повинен пройти
    task3_reduce_result_check_test(1 - 2 - 3, result)
    # Тест assert, який НЕ повинен пройти - визове виключення
    task3_reduce_result_check_test(1 - 2 - 3 + 232, result)

    # Задача 4

    loki: Animal = Cat("Loky", 4)
    bastinda: Animal = Dog("Bastinda", 9)

    print(bastinda.__dict__) # дивимося словник атрибутів екземпляру класу
    print(loki.__dict__) # дивимося словник атрибутів екземпляру класу

    print(loki.make_a_sound())
    print(bastinda.make_a_sound())


    loki.inspect() # дивимося список доступних build-методів, методів класу та змінних, доступних екземпляру класу
