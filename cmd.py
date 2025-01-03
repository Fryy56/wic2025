""" Custom module responsible for commands """
import json
import sys
from colorama import Fore


def int_test(string):
    """ Checks if the string passed is a valid int number """

    try:
        string = int(string)
    except ValueError:
        print(Fore.YELLOW + "Неверный тип аргумента.")
        print("Проверьте корректность ввода чисел-аргументов - например, "
              "год не может быть словом.")
        return "aborted"
    return string


def arg_test(arg_num, command):
    """ Checks if the number of arguments passed is within bounds or not """

    if len(command) - 1 in arg_num:
        return True
    print(Fore.YELLOW + "Подано", len(command) - 1,
          "аргументов, ожидалось:", arg_num[0], end='')
    for i in arg_num[1:]:
        print('/', i, sep="", end="")
    print()   # Skip a line
    return False


def exit_cmd():
    """
    Завершает выполнение программы.
    """

    sys.exit()


def help_cmd(command):
    """
    Выводит список всех команд сервиса/описание заданной команды (при
    поданном аргументе).

    help [%command%]

        %command% - команда для получения справки.
    """

    if len(command) == 1:
        print("""
Список команд:
[Формат: команда | алиас (если есть)]

help | h
exit
contest | c
""")
        return
    match command[1]:
        case "help":
            print(help_cmd.__doc__)
        case "exit":
            print(exit_cmd.__doc__)
        case "contest":
            print(contest_cmd.__doc__)
        case _:
            print(Fore.YELLOW + "Неизвестная команда для получения справки, "
                                "используйте `help` для просмотра списка "
                                "команд.")


def contest_cmd(contest_name, year, tasks_number, contests_dict):
    """
    Добавляет контест с заданными именем и годом, содержащий заданное
    количество задач.

    contest %contest_name% %year% %tasks_amount%

        %contest_name% - название контеста для добавления.
        %year% - год проведения контеста для добавления.
        %tasks_amount% - количество задач в контесте для добавления.
    """

    # Check for data validity
    year = int_test(year)
    tasks_number = int_test(tasks_number)
    if year == "aborted" or tasks_number == "aborted":
        return
    if tasks_number < 1:
        print(Fore.YELLOW + "Количество задач должно быть положительным.")
        return
    year = str(year)
    year = str(year)
    # Existing contest check
    if year not in contests_dict.keys():
        contests_dict[year] = []
    existing_contest = False
    existing_contest_year = None
    for key in contests_dict:
        if "data/" + contest_name + ".json" in contests_dict[key]:
            existing_contest = True
            existing_contest_year = key
    if not existing_contest:
        contests_dict[year].append("data/" + contest_name + ".json")
    else:
        confirm = 'a'
        while confirm.lower() not in ['y', 'n']:
            confirm = input(contest_name + " уже существует, заменить контест?"
                                           " Y/N >>> ")
        if confirm.lower() == 'y':
            contests_dict[existing_contest_year].remove("data/" + contest_name
                                                        + ".json")
            contests_dict[year].append("data/" + contest_name + ".json")
        else:
            print("Добавление контеста отменено.")
            return

    with open("data/_contests.json", "w", encoding="utf-8") as f:
        json.dump(contests_dict, f, indent=4)

    new_contest = {
        "tasks_number": tasks_number,
        "teams": []
    }
    with open("data/" + contest_name + ".json", "w", encoding="utf-8") as f:
        json.dump(new_contest, f, indent=4)
    print("Добавлен новый контест", contest_name + '.')
