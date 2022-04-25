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

if __name__ == "__main__":
    dict_test()