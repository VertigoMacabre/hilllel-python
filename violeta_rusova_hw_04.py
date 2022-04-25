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
    product_name: str = ""
    products_list: list = []

    print("Enter the products you want to buy. Type \"stop\" when your list is done. \n")

    while product_name.lower() != "stop".lower():
        product_name = input()
        if product_name.lower() == "stop".lower():
            break

        products_list.append(product_name.title())

    products_list.sort(key=len)

    longest_name = products_list.pop()
    letters_count = len(longest_name)

    result: str = "The longest product name from the list is {longest_product}. It contains {count_of_letters} letters".format(
        longest_product=longest_name, count_of_letters=letters_count)
    print(result)


if __name__ == "__main__":
    # task_1()
    # task_2()
    task_3()
