def task_1():
    # list comprehension

    # 1. list of integers to a list of strings
    list_of_int: list = [0, 1, 2, 3, 4, 5]
    list_of_str: list = [str(x) for x in list_of_int]
    print(list_of_str)

    # 2.  list of tuples from two lists
    my_list_1: list = ['a', 'b', 'c']
    my_list_2: list = [1, 123, 10]
    my_tuple: list = [(x, y) for x in my_list_1 for y in my_list_2]
    print(my_tuple)

    # 3. enumerate
    my_list: list = ['apple', 'milk', 'orange', 'cucumber']
    enumerated_list: list = [(a, b) for (a, b) in enumerate(my_list)]
    print(enumerated_list)

    # 4. index of a specific element
    print([c for (c, d) in enumerate(my_list) if d == 'milk'])

    # 5. if-else
    ranged_list: range = range(10)
    print(['even' if i % 2 == 0 else 'odd' for i in ranged_list])


def task_2():
    # dict comprehension
    # 1. creating dict with numbers as values
    print({str(i): i for i in [1, 2, 3, 4, 5]})

    # 2. dict from list
    my_shopping_list: list = ['apple', 'milk', 'orange', 'cucumber']
    print({f: len(f) for f in my_shopping_list})

    # 3. capitalize
    print({f: f.capitalize() for f in my_shopping_list})

    # 4. enumerate
    shoping_dict = {i: f for f, i in enumerate(my_shopping_list)}
    print(shoping_dict)

    # 5. reverse
    print({v: k for k, v in shoping_dict.items()})


def task_3():
    def pass_func():
        pass

    def doc_str():
        """doc string"""

    def good_cat(cat_name):
        print(cat_name + " is a good cat")

    good_cat("Odin")
    good_cat("Loki")
    good_cat("Arya")
    good_cat("Businka")

    #
    def odd_or_even():
        numbers_list: list = [12, 126, 15, 28, 990]
        i: int = 0
        while i < len(numbers_list):
            if numbers_list[i] % 2 != 0:
                print("Some number from the list is an odd number")
                break

            i = i + 1
        else:
            print("All numbers are even")

    odd_or_even()

    def funct_5(cat_name, cat_colour, *args, cat_sex="Male", cat_age=4, **kwargs):
        print(f"{cat_name} is {cat_colour} colored {cat_age}-aged {cat_sex}")

    funct_5('Odin', 'gray')

    def make_a_cat(name, *agrs, sex="", **kwargs):
        print(name, ars, sex, kwargs)

    make_a_cat("Loki", "orange", sex="female", age=4, legs=4, eyes=2)
    make_a_cat("Odin", "mixed colours", sex="male", age=4, legs=4, eyes=1)
    make_a_cat("Arya", "mixed colours", sex="female", age=5, legs=4, eyes=2)
    make_a_cat("Businka", "orange", sex="male", age=4, legs=4, eyes=2)


def task_4(side_of_square):
    result: tuple = (side_of_square * 4, side_of_square * side_of_square ** 0.5, side_of_square ** 2)
    print(result)


def task_5(month_num):
    seasons: dict = {
        "winter": [1, 2, 12],
        "spring": [3, 4, 5],
        "summer": [6, 7, 8],
        "autumn": [9, 10, 11],
    }

    for key, value in seasons.items():
        if value.count(month_num):
            return key


def task_6():
    first_list: list = [1, 2, 3, 4]
    second_list: list = [11, 22, 33, 44]
    result = []
    for i in first_list:
        result.append(i)

        result.append(second_list[first_list.index(i)])

    return result


def task_7():
    palindrome: str = "Полицейский Петр Павлович пускал пузыри понапрасну. Преступность побеждала"
    words: list = palindrome.lower().split()
    start_with_char = words[0][0]

    if any(w[0] != start_with_char for w in words):
        return False

    return True


if __name__ == "__main__":
    # task_1()
    # task_2()
    task_3()
    # task_4(6)
    # print(task_5(4))
    # print(task_6())
    # print(task_7())
