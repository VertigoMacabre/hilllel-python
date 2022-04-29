from termcolor import colored


# https://pypi.org/project/termcolor/
# було цікаво, чи можна розфарбувати текст

def task_1():
    users_password: str
    users_password_confirmed: str
    while True:
        users_password = input("Please enter your password. It may contain at least one number: \n")

        # https://stackoverflow.com/questions/70354803/check-if-string-contains-an-integer-python
        if not any(num.isdigit() for num in users_password):
            print(colored("Your password may contain at least one number. Please try again.\n", "red"))

        else:
            break

    while True:
        users_password_confirmed = input("Please repeat your password: \n")

        if users_password != users_password_confirmed:
            print(colored("The passwords don't match, please try again", "red"))

        else:
            print(colored("Everything is ok, the passwords match", "blue"))
            break


def task_2():
    products_list: list = ['beer', 'milk', 'egg', 'egg', 'egg', 'egg']
    while products_list.count("egg"):
        products_list.remove("egg")

    print(products_list)


def task_3():
    numbers_list: list = [12, 126, 15, 28, 990]
    i: int = 0
    while i < len(numbers_list):
        if numbers_list[i] % 2 != 0:
            print("Some number from the list is an odd number")
            break

        i = i + 1
    else:
        print("All numbers are even")


def task_4():
    objects: list = [set, int, str, tuple, dict, list]
    result: dict = {}

    # https://www.adamsmith.haus/python/answers/how-to-check-if-a-list-contains-a-substring-in-python
    """до речі. думала, де ж я бачила вже конструкцію list comprehension, по ходу тут? чи я не права? 
    альтеранивний метод тут виглядає як list comprehension"""

    for o in objects:
        methods_list: list = dir(o)
        substring = "_"

        while any(substring in method for method in methods_list):
            for method in methods_list:
                if method.count(substring):
                    methods_list.remove(method)

        # https://stackoverflow.com/questions/1538342/how-can-i-get-the-name-of-an-object
        result[o.__name__] = methods_list

    while True:
        name: str = input("Input object type name in [set, int, str, tuple, dict, list]: \n")

        if name == "stop":
            break

        if any(name == o.__name__ for o in objects):
            print(f"There are such available methods for Python object '{name}':\n", result[name])
        else:
            print(colored("Unsupported object type name.", "red"))
        print("\n")


def task_4_1():

    # ще знайшла такий спосіб

    methods_list: list = dir(set)
    substring = "_"
    filtered = []

    for method in methods_list:
        if method.count(substring) == 0:
            filtered.append(method)

    print(filtered)

def task_4_2():
    # після 6 заняття, де як раз розбирали list comprehension, вирішила додати ще один варіант вирішення

    methods_list: list = dir(set)
    substring = "_"

    methods_list_with_substring = [string for string in methods_list if substring not in string]
    print(methods_list_with_substring)


def task_5():
    # https://realpython.com/quizzes/python-lists-tuples/results/?t=eyJjIjoxMSwibiI6MTEsInEiOjcsInNpZyI6IjJqdkRxSWV0NjIzYjNSPz52Klleb09FNkI4I0JOWXhsPXhOVkQtISkiLCJ0IjoyMzIsInYiOjN9&s=1
    # https://realpython.com/quizzes/python-sets/results/?t=eyJjIjoxMCwibiI6MTAsInEiOjExLCJzaWciOiI0TEd1WHpEfUN5dE1rMWNBKGVKa1VTT29-JVVaV3BgTyt3VjIxZX14IiwidCI6MjIyLCJ2IjozfQ==&s=1
    pass


def task_6():
    main_set: set = {1, 2, 3}
    additional_set: set = {'a', 'b', 'citrus'}
    additional_set2: set = {'citrus', 'Elon Musk', 'doge'}

    # len
    print(f"Size of main_set is: {len(main_set)}")

    # remove
    main_set.remove(2)
    print(main_set)

    # add
    main_set.add(2)
    print(main_set)

    # update
    main_set.update([2, 3, 4, 5])
    print(main_set)

    # discard
    main_set.discard(1)
    print(main_set)

    """Далі у коментах приводжу варіант через оператори
    Різницю між застосуванням методів та операторів розумію: 
    1. через метод ми можемо щось зробити з двома сетами, а через оператор - з декількома
    2. """

    # union
    union_result: set = (main_set.union(additional_set))
    print(union_result)
    # union_result: set = main_set | additional_set
    # print(union_result)

    # intersection
    print(union_result.intersection(additional_set2))
    # intersection_result: set = union_result & additional_set2
    # print(intersection_result)

    # difference
    difference_result: set = union_result.difference(additional_set2)
    print(difference_result)
    # difference_result: set = union_result - additional_set2
    # print(difference_result)

    # symmetric_difference
    symmetric_difference_result: set = union_result.symmetric_difference(additional_set2)
    print(symmetric_difference_result)
    # symmetric_difference_result: set = union_result ^ additional_set2
    # print(symmetric_difference_result)

    # isdisjoint
    isdisjoint_result: bool = union_result.isdisjoint(additional_set2)
    print(isdisjoint_result)

    # in
    if 1 in main_set:
        print("1 is in main set")
    else:
        print("1 is not in set")


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_4_1()
    # task_4_2()
    # task_5()
    # task_6()
