def task_1():
    input_string: str = "Hillel school"
    result: str = "%s%s" % (input_string[0:2:], input_string[-2::])

    if len(result) < 2:
        print("String \"%s\" to short" % result)

    print("Result is \"%s\"" % result)


def task_2():
    input_string: str = "Hillel school"
    letters_count: dict = {}

    for char in input_string:
        letters_count[char] = input_string.count(char)

    print(letters_count)


def task_3():

    products_list: list = []

    print("Enter the products you want to buy. Type \"stop\" when your list is done. \n")

    while True:
        product_name: str = input()
        if product_name.lower() == "stop".lower():
            break

        products_list.append(product_name.title())

    products_list.sort(key=len)

    longest_name = products_list.pop()
    letters_count = len(longest_name)

    result: str = "The longest product name is {longest_product}. It contains {count_of_letters} letters".format(
        longest_product=longest_name, count_of_letters=letters_count)
    print(result)


def task_4():
    user_name: str = input("Please enter your name \n")
    result: str = "{name_cap} {name_low}".format(name_cap=user_name.upper(), name_low=user_name.lower())
    print(result)


def task_5():
    list_of_items: list = input("Please enter some words \n").lower().split()
    list_of_unique_items = list(set(list_of_items))
    list_of_unique_items.sort()
    print(list_of_unique_items)


def task_6():
    data: tuple = (1, 2, 3)
    print(data[:-1])


def task_7():
    list_of_tuples: tuple = tuple([(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)])
    list_of_lists = [list(item) for item in list_of_tuples]
    print(list_of_lists)


def task_8():
    range_of_numbers: tuple = tuple(range(-99, 99, 3))
    print(range_of_numbers)
    for i in range_of_numbers:
        if i % 3 == 0:
            print(f"это {i} делится без остатка на 3")


def task_9():
    list_1: list = [18, "orange", "yellow", "asdf", 3, 3.67]
    list_2: list = ["darth vader", 1, 7, "orange"]

    for element in list_1:
        if list_2.count(element) > 0:
            print(True)
            break


if __name__ == "__main__":
    # task_1()
    # task_2()
    task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    # task_9()
