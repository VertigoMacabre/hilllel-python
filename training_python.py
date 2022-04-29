def dict_test():
    person: dict = {}
    input_string: str = "Віолета Русова Hillel Python 5 4 5 5 5"
    result: [] = input_string.split()
    print(result)
    person["last_name"] = result[1]
    person["first_name"] = result[0]
    person["school"] = result[2]
    person["course"] = result[3]
    person["marks"] = []
    for key in result[4:]:
        person["marks"].append(int(key))

    if "sex" in person:
        print("ключ sex у списку person")
    else:
        person["sex"] = "Female"

    print(person)


def while_test_1():
    i = 1
    while i <= 10:
        c: int
        if i % 2 != 0:
            c = i + 2
        else:
            c = i * 2
        print(c)
        i = i + 1


def while_test_2():
    i = 1
    while True:
        print(f'Iteration N{i}')
        if i == 10:
            break
        i += 1
        print('break not work here')
    print('after While')


if __name__ == "__main__":
    # dict_test()
    # while_test_1()
    # while_test_2()

    methods = dir([])
    substring = "_"

    # https://www.adamsmith.haus/python/answers/how-to-check-if-a-list-contains-a-substring-in-python
    while any("_" in method for method in methods):
        for method in methods:
            if method.count(substring):
                methods.remove(method)




    print(methods)
