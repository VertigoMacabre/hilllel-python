def task_1():
    """прочитать Глава № 32 Основы исключений. 918-927 Lutz. 20 баллов
    - Зроблено. Не зайшла мені його подача інформації, нажаль((
    За інфою зверталася до
    https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
    https://www.programiz.com/python-programming/exceptions"""
    pass


def task_2():
    # try\except
    # try\finally

    def zero_dividing() -> None:
        try:
            a: int = int(input("Enter a: "))
            b: int = int(input("Enter b: "))
            c: float = a / b
            print(c)
        except ZeroDivisionError:
            print("Can't divide with zero")
        finally:
            print("Remember, kids, you are not authorized to divide by zero")

    zero_dividing()

    # raise exception

    class WrongPlaceError(Exception):
        pass

    def set_a_building() -> None:
        while True:
            try:
                place: str = input("Where do you want to place your building: city/village/Mars?\n").lower()
                if place == "city":
                    print("So, you chose to build up in a city. We can place your building here!")
                elif place == "village":
                    print("So, you want to live in a country side? Okay, we can place your building here.")
                elif place == "moon":
                    print("Nope, sorry. Elon Musk haven't colonized Mars yet. You should wait for a couple of years :(")
                else:
                    raise WrongPlaceError

            except WrongPlaceError:
                print("Choose from what you should to, dude")

    set_a_building()


def task_3():
    """написать функцию которая принимает от пользователя 2 аргумента и делит онин на другой.
при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"""

    def operating_numbers() -> None:
        while True:
            try:
                x: int = int(input("Введи x: "))
                y: int = int(input("Введи y: "))
                result: float = x / y
                print(result)
            except ZeroDivisionError:
                print("ай-яй-яй! делить на ноль можно немногим")
            except ValueError as e:
                print(f"{e}.\n таки введи целое(!) число(!)")
            except Exception:
                print("ты поломал то, что я сама не смогла придумать, как поломать, мои поздравления")
            finally:
                print("в любом случае, классно, что ты учишь python :)")

    operating_numbers()


def task_4():
    """скрін проходження тесту прикріплений до домашки"""
    pass


# Далі починається завдання 5. Ітератор винесла як клас у global, бо інакше ніяк
class HelloWorld:  # буде повертати фразу стільки раз, скільки задамо
    def __init__(self, num_iters):  # ітероване / iterable
        self.num_iters = num_iters
        self.counter = 0  # лічильник, буде рахувати, скільки ми з потрібних ітерацій зробили

    def __iter__(self):  # ітератор / iterator
        return self  # повертає сам об'єкт, бо він вже являється ітератором

    # ітератор та ітерабельне іноді розділяють за різними класами, але тут можна в один

    def __next__(self):  # метод __next__ повертає наступний елемент у послідовності
        if self.counter < self.num_iters:  # перевіряємо лічильник, чи він є меншим, ніж потрібна кіл-ть ітерацій
            self.counter += 1  # якщо так, збільшуємо на 1
            return "Hello World!"
        raise StopIteration  # інакше - підіймаємо ексепшн, якщо дійшли до межі ітерацій


def task_5():
    """Попробовать понять. Патерн Итератор https://refactoring.guru/ru/design-patterns/iterator/python/example"""
    # Ітератори можуть повертати якісь дані один за одним
    # заміняють складнішу конструкцію for in, перебираючи елементи колекції
    # Наприклад, такі: list, tuple, dict, sets, str
    # Ітерований об'єкт - iterable, те, над чим виконується ітерація
    # Ітератор - iterator, те, що виконує ітерацію
    # В ітератора є атрибути:
    # _position: int - вказує, з якого елемента послідовності ми хочемо розпочати
    # _reverse: bool - напрямок, у якому ми будемо перебирати елементи
    # Під час роботи з ітераторами важливо перебачити exception StopIteration
    # щоб при досягненні кінця колекції в нас все не зламалося з помилкою IndexError

    """далі звертаємося до оголошеного раніше в global ітератора HelloWorld"""

    greeter = HelloWorld(6)
    for item in greeter:
        print(item)

    # все працює :)

    # Окремі колекції надають специфічні методи для отримання нових екземплярів ітератора, сумісних з їх класом
    # Наприклад, метод AlphabeticalOrderIterator (сортує за алфавітом) з атрибутами _position: int та _reverse: bool


def task_6():
    def example1() -> None:
        try:
            for i in range(3):
                x = int(input("enter a number: "))
                y = int(input("enter another number: "))
                print(x, '/', y, '=', x / y)
                break
        except ValueError as e:
            print(f"{e}.\n таки введи целое(!) число(!)")
        except ZeroDivisionError as e:
            print(f"{e}.\nай-яй-яй! делить на ноль можно немногим")
        except Exception:
            print("ты поломал то, что я сама не смогла придумать, как поломать, мои поздравления")

    example1()

    def example2(l) -> None:
        print("\n\nExample 2")
        sum: int = 0  # а це тут нащо??
        sumOfPairs: list = []
        try:
            for i in range(len(l)):
                sumOfPairs.append(l[i] + l[i + 1])
                print("sumOfPairs = ", sumOfPairs)

        except IndexError as e:
            print(e)


        except TypeError as e:
            print(e)

    try:
        l: list = [10, 3, 5, 6, 9, 3]
        example2(l)
        example2([10, 3, 5, 6, "NA", 3])
        example3([10, 3, 5, 6])

    except NameError as e:
        print(f"а такой функции то и нет! {e}")

    def printUpperFile(fileName) -> bool:
        try:
            file = open(fileName, "r")
        except FileNotFoundError:
            print("***Error*** File:", fileName, "not found!")
            return False

        for line in file:
            print(line.upper())
        file.close()
        return True

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
