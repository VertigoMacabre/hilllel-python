# погуглила бібліотеку datetime, знайшла https://www.programiz.com/python-programming/datetime/current-datetime
# там там не було саме з year, знайшла тут https://reactgo.com/python-get-current-year/#:~:text=To%20get%20the%20current%20year%20in%20Python%2C%20first%20we%20need,to%20the%20user%27s%20local%20time.

from datetime import date


def hw_03_task_1():
    year_of_birth = input("Year of births?\n")
    print(year_of_birth)

    # погуглила, як перевірити  число це чи не число
    # https://www.tutorialsteacher.com/python/string-isdigit#:~:text=Python%20String%20isdigit()%20Method,If%20not%2C%20it%20returns%20False
    while not year_of_birth.isdigit():
        print('Year of births is not a number, try again\n')
        year_of_birth = input("Year of births?\n")

    else:
        current_year: int = date.today().year
        age: int = current_year - int(year_of_birth)

        if age == 21:
            print("You should visit Holland.\n")

        elif age > 21:
            print("You should visit Vietnam.\n")

        else:
            print("Travel everywhere")


def hw_03_task_2():
    nick_name: str = input("What is your name ?\n")

    # щоб перевірити, чи строка вміщує master у різних регістрах, переводимо все у нижній регістр
    if nick_name.lower().count("master") > 0:
        print("Welcome to dark side\n")

    age: int = int(input("How old are you?\n"))
    sex: str = input("Sex (M/F)?\n").lower()
    available_sex: [] = ["m", "f"]

    print(nick_name, age, sex.upper(), sep=" `", end=".\n")

    while not available_sex.count(sex):
        print("Unavailable sex, try again\n")
        sex: str = input("Sex (M/F)?\n").lower()

    if ((10 <= age <= 14) or age > 30) and sex == "m":
        print("Recommended to watch \"Start Wars\" or The \"Mandalorian\"")

    elif (22 <= age <= 32) and sex == "m":
        print("Recommended to watch \"Transformers\"")

    elif (age <= 16) and sex == "f":
        print("Recommended to watch \"Insurgent\"")

    elif nick_name.lower() == "женя":
        print("Recommended to watch \"TENET\"")

    elif (age <= 11) and sex == "m":
        print("Recommended to watch \"TMNT\"")

    else:
        print("No recommendations to you, sorry\n")

    if nick_name.lower() == "guido":
        print("Thnx\n")


def hw_03_task_3():
    source_string = "(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$"
    print(source_string[::5])


def hw_03_task_4():
    days_in_sol = 1.02595675
    input_str: str = input("Enter days and hours via \",\" separator \n")
    input_time = input_str.split(", ")

    earth_days: int = int(input_time[0])
    earth_hours: int = int(input_time[1])

    result = round((earth_days + earth_hours / 24) / days_in_sol, 2)
    print(f"{earth_days} days and {earth_hours} hours on Earth equals to {result} Martian sols")


def hw_03_task_5():
    input_str: str = "черт его возьми, черт его знает, Чертополох, иди к черту, черт ногу сломит, Чертеж здания в разрезе"
    # print(re.sub("черт", "####", input_str))
    print(input_str.replace("черт", "####", input_str.count("черт")))


if __name__ == "__main__":
    # hw_03_task_1()
    # hw_03_task_2()
    # hw_03_task_3()
    # hw_03_task_4()
    hw_03_task_5()
