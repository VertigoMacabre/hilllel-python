from datetime import datetime

import requests


def task_1():
    students_list: list = [
        {
            "name": "Leta",
            "age": 34,
            "course": "Python",
            "avg_mark": 4,
            "species": "human",
        },
        {
            "name": "Businka",
            "age": 4,
            "course": "Python",
            "avg_mark": 0,
            "species": "cat"
        },

        {
            "name": "Anton",
            "age": 35,
            "course": "Dart",
            "avg_mark": 5,
            "species": "human"
        }
    ]
    ### All ###
    are_all_humans: bool = all(student['species'] == 'human' for student in students_list)
    print(f"Are all students humans? - {are_all_humans}")
    age_from_30: bool = all(student['age'] >= 30 for student in students_list)
    print(f"Are all students are above 30? - {age_from_30}")
    learning_python: bool = all(student['course'] == 'Python' for student in students_list)
    print(f"Are all students learn Python? - {learning_python}")

    ### Sort ###
    # students_list.sort(key=lambda student: student['name'])
    # print(students_list)

    ### Filter ###
    human_students: list = list(filter(lambda student: student['species'] == 'human', students_list))
    print("Human students are: ", human_students)
    cat_students: list = list(filter(lambda student: student['species'] == 'cat', students_list))
    print(f"These students are cats. They have paws and obviously can not code", cat_students)
    students_above_30: list = list(filter(lambda student: student['age'] >= 30, students_list))
    print("These students are pretty old", students_above_30)

    ### Any ###
    lagging_behind_students_exists: bool = any(student['avg_mark'] <= 4 for student in students_list)
    print(f"Does anyone lag behind? - {lagging_behind_students_exists}")
    students_learning_python: bool = any(student['course'] == 'Python' for student in students_list)
    print(f"Does anyone learn Python? - {students_learning_python}")
    students_learning_java: bool = any(student['course'] == 'Java' for student in students_list)
    print(f"Does anyone learn Java? - {students_learning_java}")


def task_2():
    def counting_bottles(x: int):
        if x > 1:
            print(f"{x} bottles of beer left")
            x -= 1
            counting_bottles(x)
        elif x == 1:
            print(f"{x} bottle of beer left")
            x -= 1
            print("No more bottles left, go to beer store")

    counting_bottles(20)

    def feeding_cat(snacks: int):
        input_snacks_to_feed = int(input(f"A cat is hungry. Enter a number "
                                         f"of snacks you want to give him ({snacks} left)\n"))

        if not bool(input_snacks_to_feed):
            feeding_cat(snacks)

        snacks = snacks - int(input_snacks_to_feed)

        if snacks > 0:
            feeding_cat(snacks)
        else:
            print("A cat is fed and very grateful.")

    x = 5
    feeding_cat(x)

    def fibonacci_numbers(x: int = 1, y: int = 1):
        if x > 100:
            return
        if x < 2:
            print(1)
        else:
            print(x)
        fibonacci_numbers(y, y + x)

    fibonacci_numbers()


"""Рекурсивна функція визиває сама себе (тобто починається з початку себе) 
й може робити це безкінечно (якщо не додати умови, за якої вона закінчиться).
Вона може визивати себе, бо функція це такий самий об'єкт як й змінні. Й цей об'єкт є у її області видимості
(є у її NameSpace)"""


def task_3():
    # ##### Var 1 ####

    def execution_time(function):
        def wrapper(**kwargs):
            start = datetime.now()
            answer = function(**kwargs)
            print(datetime.now() - start)
            return answer

        return wrapper

    @execution_time
    def sort_wrapper():
        fibonacci_numbers()

    def fibonacci_numbers(x: int = 1, y: int = 1):

        if x > 10000:
            return
        if x < 2:
            print(1)
        else:
            print(x)
        fibonacci_numbers(y, y + x)

    sort_wrapper()

    #### Var 2 ####

    def time_took_to_sort(function):
        def wrapper():
            start = datetime.now()
            function()
            finish = datetime.now() - start
            print("Time to sort: ", finish)

        return wrapper

    @time_took_to_sort
    def sorting_students_list():
        students_list: list = [
            {
                "name": "Leta",
                "age": 34,
                "avg_mark": 4.5,
                "species": "human",
            },
            {
                "name": "Businka",
                "age": 4,
                "avg_mark": 2,
                "species": "cat"
            },

            {
                "name": "Anton",
                "age": 35,
                "avg_mark": 3,
                "species": "human"
            },
        ]

        students_list.sort(key=lambda student: student['name'])

    sorting_students_list()

    ##### Var 3 ####

    def execution_time_fetch(function):
        def wrapper():
            start = datetime.now()
            function()
            finish = datetime.now() - start
            print(("Fetch webpage", finish))

        return wrapper

    @execution_time_fetch
    def fetch_webpage():
        requests.get('https://google.com')

    fetch_webpage()


"""Декоратор приймає функцію, додає їй певну функціональність і повертає її.
Це простий спосіб розширити функціональність наших оригінальних функцій,
не змінюючи їх вихідний код.

Згідно з Single Responsibility Principle функція має виконувати одну задачу.
Тому, якщо ми хочемо додати функціоналу у вже існуючу функцію, краще не пхати його прям до неї.
Ми маємо додати його через окрему декоруючу функцію
"""

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
