import sys

from termcolor import colored


def task_1():
    users_password_1: str
    users_password_2: str
    while True:
        users_password_1 = input("Please enter your password. It may contain at least one number: \n")

        if not any(num.isdigit() for num in users_password_1):
            print(colored("Your password may contain at least one number. Please try again.\n", "red"))

        else:
            break

    while True:
        users_password_2 = input("Please repeat your password: \n")

        if users_password_1 != users_password_2:
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
    numbers_list: list = [12, 126, 14, 28, 990]
    i: int = 0
    while i <= len(numbers_list) - 1:
        if numbers_list[i] % 2 != 0:
            print("Some number from the list is an odd number")
            break
        else:
            i = i + 1
    else:
        print("All numbers are even")


def task_4():
    objects: list = [set, int, str, tuple, dict, list]
    result: dict = {}

    # https://www.adamsmith.haus/python/answers/how-to-check-if-a-list-contains-a-substring-in-python
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
        name = input("Input object type name in [set, int, str, tuple, dict, list] \n")

        if name == "stop":
            break

        print(f"There are such available methods for Python object '{name}':\n", result[name])


def task_4_1():
    methods_list = dir(set)
    # https://www.adamsmith.haus/python/answers/how-to-check-if-a-list-contains-a-substring-in-python
    substring = "_"
    filtered = []

    for method in methods_list:
        if method.count(substring) == 0:
            filtered.append(method)

    print(filtered)


def task_5():
    # https://realpython.com/quizzes/python-lists-tuples/results/?t=eyJjIjoxMSwibiI6MTEsInEiOjcsInNpZyI6IjJqdkRxSWV0NjIzYjNSPz52Klleb09FNkI4I0JOWXhsPXhOVkQtISkiLCJ0IjoyMzIsInYiOjN9&s=1
    pass


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    task_4()
    # task_4_1()
    # task_5()
