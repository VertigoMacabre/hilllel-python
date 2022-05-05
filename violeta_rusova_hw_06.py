from collections import ChainMap


def task_1():
    # Using ** operator

    # first_dict: dict = {1: 10, 2: 20}
    # second_dict: dict = {3: 30, 4: 40}
    # third_dict: dict = {5: 50, 6: 60}
    # fourth_dict: dict = {7: 70, 8: 80}
    # fifth_dict: dict = {9: 90, 10: 100}
    # merged_dict: dict = {**first_dict, **second_dict, **third_dict, **fourth_dict, **fifth_dict}
    # print(merged_dict)

    # Using collection.ChainMap() method

    # ChainMap()
    # ChainMap({})
    # first_dict: dict = {1: 10, 2: 20}
    # second_dict: dict = {3: 30, 4: 40}
    # third_dict: dict = {5: 50, 6: 60}
    # fourth_dict: dict = {7: 70, 8: 80}
    # fifth_dict: dict = {9: 90, 10: 100}
    #
    # merged_dict: dict = ChainMap(first_dict, second_dict, third_dict, fourth_dict, fifth_dict)
    # print(dict(merged_dict))

    # Using dictionary comprehension

    first_dict: dict = {1: 10, 2: 20}
    second_dict: dict = {3: 30, 4: 40}
    third_dict: dict = {5: 50, 6: 60}
    fourth_dict: dict = {7: 70, 8: 80}
    fifth_dict: dict = {9: 90, 10: 100}
    merged_dict: dict = {k: v for d in
                         (first_dict, second_dict, third_dict, fourth_dict, fifth_dict) for k, v in d.items()}
    print(merged_dict)


def task_2():
    num_dict: dict = {}

    for i in range(11, 21):
        num_dict[i] = i ** 2
    print(num_dict)

    sum_values: int = sum(list(num_dict.values()))
    print(sum_values)


def task_3():
    to_watch_list: dict = dict(zip(
        ["tv_shows", "cartoons", "movies", "anime"],
        [
            ["Stargate SG-1", "Torchwood"],
            ["Infinity Train", "Bravest Warriors", "Invader Zim"],
            "Batman 2022",
            ["Evangelion Remastered", "Attack on Titan"]
        ]
    )
    )

    sorted_to_watch_list = dict(sorted(to_watch_list.items()))
    print(sorted_to_watch_list)


def task_4():
    students_info: dict = {
        "id1": {
            "class": 1,
            "name": "Ruslan",
            "subjects": {
                "Math",
                "Algorithms",
                "English",
            }
        },
        "id2": {
            "name": "Mark",
            "class": 2,
            "subjects": {
                "Geometry",
                "Java",
                "Cooking"
            }
        },
        "id3": {
            "name": "Ruslan",
            "class": 1,
            "subjects": {
                "Math",
                "Algorithms",
                "English"
            }
        }
    }

    unique_students_info_list: dict = {}

    for key in students_info:
        if students_info[key] in unique_students_info_list.values():
            continue
        else:
            unique_students_info_list[key] = students_info[key]

    print(unique_students_info_list)

    # інше рішення
    #
    # while any(list(students_info.values()).count(info) > 1 for info in students_info.values()):
    #     for key in students_info.copy().keys():
    #
    #         if list(students_info.values()).count(students_info[key]) > 1:
    #             del students_info[key]
    #
    # print(students_info)


def task_5():
    non_unique_dict: list = [{"V": "S001"}, {"V": "S002"},
                             {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    unique_values: set = set(val for d in non_unique_dict for val in d.values())
    print("Unique values are: ", unique_values)


def task_6():
    schedule: dict = {
        'monday': ['clean house', 'drive car', 'meet with friends'],
        'tuesday': None,
        'wednesday': ['manicure', 'hammam', 'beer']
    }

    print(sum(len(schedule[day]) for day in schedule if schedule[day]))


# вирішила ускладнити завдання, щоб потренуватися ще
def task_6a():
    schedule: dict = {
        'monday': {
            "morning": [
                'clean house',
                'meet with friends'
            ],
            "afternoon": [
                'drive a car'
            ],
            "evening": [
                'meet with friends']
        },
        'tuesday': None,
        'wednesday': {
            "morning": ['manicure'],
            "afternoon": ['hammam'],
            "evening": ['beer']
        }

    }

    print(sum(len(schedule[day][time]) for day in schedule if schedule[day] for time in schedule[day]))


def task_6b():
    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    pass


if __name__ == "__main__":
    # task_1()
    # task_2()
    task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_6a()
    # task_6b()
