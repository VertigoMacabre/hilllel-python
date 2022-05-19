def task_0() -> ():  # відео подивилася

    """Видосик по Замыканиям просмотреть
    и повторить за автором. мне скинуть файлик с повтором или своим примером"""


def main_func(raise_power_to) -> ():
    def inner_func(number) -> int:
        return number ** raise_power_to

    return inner_func


raise_power = main_func(4)
print(raise_power.__closure__[0].cell_contents)


def task_1():
    """Написать функцию которая будет добовлять код страны к номеру телефона с помощью замыкания"""

    #   Var 1
    # def phone_number(input_number: str) -> ():
    #     def add_county_code(country_code) -> str:
    #         return country_code + input_number
    # 
    #     return add_county_code
    # 
    # print(phone_number('838372893')("+044"))

    #   Var 2
    def user_phone(country_code) -> ():
        def add_county_code(input_number) -> str:
            return country_code + input_number

        return add_county_code

    phone = user_phone("+044")
    print(phone("838372893"))


def task_2_3():
    """Task 2: Написать функцию которая будет у пользователя брать python обект в любом виде и выводить
    все его не магические методы в списке. и написать декторатор который будет выводить колличество методов в объекте.

    Task 3: дописать декоратор, чтобы он принимал аргумент, например текст. и выводил его тоже."""

    def counting(message) -> ():

        def set_wrapper_message(function):
            def wrapper(*args) -> list:
                answer = function(*args)
                print(f"{message} {len(answer)}")
                return answer

            return wrapper

        return set_wrapper_message

    @counting("Amount of non-magic methods is:")
    def get_non_magic_methods(obj: type) -> list:
        return list(filter(lambda method: method.count("__") == 0, dir(obj)))

    while True:
        try:
            input_object_name: str = input("Enter object name \n")
            # підказали простіше рішення, ніж в мене було у попередній задачі, через eval
            # https://proglib.io/p/dinamicheskoe-vypolnenie-vyrazheniy-v-python-funkciya-eval-2020-05-14
            created_object: str = eval(input_object_name)

            if isinstance(created_object, type):
                non_magic_methods = get_non_magic_methods(created_object)
                print(non_magic_methods)
            else:
                print("Not a type")

        except Exception:

            print("Something went wrong :(")


def task_4():
    """Ваша задача - создать декоратор для функции, которая принимает неограниченное количество
    позиционных ХЕШИРУЕМЫХ элементов. Декоратор добавляет следующий функционал:
    Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат
    выполнения этой функции из памяти, а не вычислять его заного.
    Если не вызывалась - вычислить результат, положить его в память, и вернуть."""

    hash_set: dict = {}

    def hashable(function) -> ():
        def wrapper(*args) -> set:
            args_hash: int = hash(args)

            if args_hash in hash_set:
                print("Result from hash")
                return hash_set[hash(args)]

            result = function(args)
            hash_set[args_hash] = result
            print("Result added in hash")
            return result

        return wrapper

    @hashable
    def do_something_function(*args) -> set:
        return args

    print(do_something_function(1, 2, 3, 4, 5))
    print(do_something_function(1, 2, 3, 4, 10, "sss"))
    print(do_something_function(1, 2, 3, 4, 10, "sss"))


if __name__ == '__main__':
    task_0()
    task_1()
    # task_2_3()
    # task_4()
