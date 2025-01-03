# Modules   pylint: disable=missing-module-docstring
import sys
import json
import cmd
from colorama import init, Fore


# Functions
def input_parse(split_list):
    """ Parses a list as a split string while keeping quoted parameters """

    quote_check = False
    quotes_list = ['"', "'", '“', '”', '«', '»', '„', '”']
    i = 0
    while i <= len(split_list):
        if len(split_list) - 1 < i:
            break
        if quote_check:
            if split_list[i][-1] in quotes_list:
                quote_check = False
                split_list[i] = split_list[i][:-1]
            split_list[i - 1] += ' ' + split_list[i]
            split_list.pop(i)
        else:
            if split_list[i][0] in quotes_list:
                if split_list[i][-1] in quotes_list:
                    split_list[i] = split_list[i][1:-1]
                else:
                    quote_check = True
                    split_list[i] = split_list[i][1:]
            i += 1
    return split_list


init()   # Initialize colorama for color compatibility
print("Инициализация списка контестов...")
try:
    with open("data/_contests.json", "r", encoding="utf-8") as f:   # JSON init
        try:
            contests = json.load(f)
        except json.decoder.JSONDecodeError:
            print(
                Fore.RED + "Ошибка чтения файла data/_contests.json. Убедитесь"
                           ", что файл имеет корректное содержимое.\n")
            input(Fore.RESET + "Нажмите ENTER для завершения программы.")
            sys.exit()
        else:
            print("Список загружен, введите команду.")
except FileNotFoundError:
    print(Fore.RED + "Ошибка чтения файла data/_contests.json. Убедитесь, "
                     "что файл существует.\n")
    input(Fore.RESET + "Нажмите ENTER для завершения программы.")
    sys.exit()

while True:   # Main input loop
    command = input(Fore.RESET + ">>> ").split()
    command = input_parse(command)
    try:
        command_header = command[0]
    except IndexError:
        continue

    match command_header:
        case "exit":
            if cmd.arg_test([0], command):
                cmd.exit_cmd()
        case "help" | "h":
            if cmd.arg_test([0, 1], command):
                cmd.help_cmd(command)
        case "contest" | "c":
            if cmd.arg_test([3], command):
                cmd.contest_cmd(command[1], command[2], command[3], contests)
            else:
                print("Проверьте корректность кавычек вокруг параметров, "
                      "например Имя контеста воспринимается как 2 параметра, в"
                      " то время как \"Имя контеста\" - как 1.")
        case "submit" | "s":
            try:
                with open("data/" + command[2] + ".json",
                          encoding="utf-8") as f:
                    try:
                        cur_contest = json.load(f)
                    except json.decoder.JSONDecodeError:
                        print(
                            Fore.RED + "Ошибка чтения файла контеста. Убедите"
                                       "сь, что файл имеет корректное содержи"
                                       "мое.")
                        continue
            except FileNotFoundError:
                print(
                    Fore.RED + "Ошибка чтения файла контеста. Убедите"
                               "сь, что файл существует.")
                continue
            if cmd.arg_test([int(cur_contest["tasks_number"]) + 2],
                            command):
                cmd.submit_cmd(command[1], command[2], command[3:],
                               cur_contest)
            else:
                print("Проверьте корректность кавычек вокруг параметров, "
                      "например Имя контеста воспринимается как 2 параметра, в"
                      " то время как \"Имя контеста\" - как 1.")
        case _:
            print(Fore.RED + "'", command_header, "' - не команда сервиса. "
                  "Используйте `help` для просмотра списка команд.", sep='')
