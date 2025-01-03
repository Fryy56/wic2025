""" Custom module responsible for commands """
import sys
from colorama import Fore


def arg_test(arg_num, command):
    """ Checks if the number of arguments passed is within bounds or not """

    if len(command) - 1 in arg_num:
        return True
    print(Fore.YELLOW + "Подано", len(command) - 1,
          "аргументов, ожидалось:", arg_num[0], end='')
    for i in arg_num[1:len(arg_num)]:
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
(Формат: команда | алиас (если есть))

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
        case _:
            print(Fore.YELLOW + "Неизвестная команда для получения справки, "
                                "используйте `help` для просмотра списка "
                                "команд.")
