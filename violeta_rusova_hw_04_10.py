import sys

storage: list = [
    [None] * 5,
    [None] * 5,
    [None] * 5,
    [None] * 5,
    [None] * 5,
]


def show_storage():
    rows = 5
    cols = 5

    print("+---+---+---+---+---+")
    for row in list(range(rows)):

        row_strint = ""

        for col in list(range(cols)):
            if storage[row][col]:
                mark = "*"
            else:
                mark = " "

            row_strint += f"| {mark} "

        print(row_strint + "|")
        print("+---+---+---+---+---+")


def record_exist(x: int, y: int):
    return storage[x - 1][y - 1]


def set_record(x: int, y: int, value):
    storage[x - 1][y - 1] = value


def get_record(x: int, y: int):
    return storage[x - 1][y - 1]


def delete_record(x, y):
    storage[x - 1][y - 1] = None


def make_dialog():
    while True:

        answer: str = input("Выбери действие:\n"
                            + "1) Сделать запись\n"
                            + "2) Получить значение по координатам\n"
                            + "3) Показать все ячейки\n"
                            + "4) Удалить значение по координатам\n"
                            + "0) Программа завершает работу.\n")

        if answer == "1":
            input_data: list = input("Введите x и y в формате x y value\n").split()
            x, y, value = int(input_data[0]), int(input_data[1]), input_data[2]

            if record_exist(x, y):
                answer: str = input("Запись существует. Перезаписать ?\n"
                                    + "1) Да.\n"
                                    + "2) Нет.\n")

                if answer == "1":
                    set_record(x, y, value)
                    show_storage()

                else:
                    break

            else:
                set_record(int(input_data[0]), int(input_data[1]), input_data[2])
                print("Запись сделана!\n")
                show_storage()

        if answer == "2":
            input_data: list = input("Введите x и y в формате x y value\n").split()
            x, y, = int(input_data[0]), int(input_data[1])
            record = get_record(x, y)

            if record:
                print(record)
            else:
                print("Пустая ячейка\n")

        if answer == "3":
            show_storage()

        if answer == "4":
            input_data: list = input("Введите x и y в формате x y value\n").split()
            x, y, = int(input_data[0]), int(input_data[1])
            delete_record(x, y)
            print("Запись удалена!\n")
            show_storage()

        if answer == "0":
            sys.exit()


if __name__ == "__main__":
    show_storage()
    make_dialog()
