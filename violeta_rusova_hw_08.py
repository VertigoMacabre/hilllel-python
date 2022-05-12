from datetime import datetime


def task_1(x: int, y: int, z: int) -> int:
    result: int = max(x, y, z)
    print(result)
    return result


def task_2():
    def max_of_two(x: int, y: int):
        result: int = max(x, y)
        return result

    def max_of_three(x: int, y: int, z: int):
        middle = max_of_two(x, y)
        return max_of_two(middle, z)

    print(max_of_three(5, 6, 1))


def task_3():
    list_of_products: list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
    list_of_products.sort(key=lambda val: val[1])
    print(list_of_products)


def task_4():
    now = datetime.now()
    print(now)
    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    time = lambda x: x.time()
    print(year(now))
    print(month(now))
    print(day(now))
    print(time(now))



if __name__ == "__main__":
    # task_1(1, 2, 34)
    # task_2()
    # task_3()
    task_4()
