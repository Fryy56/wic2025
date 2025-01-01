""" Custom module responsible for commands """
import sys
from colorama import Fore


def arg_test(arg_num, command):   # pylint: disable=missing-function-docstring
    if len(command) - 1 == arg_num:
        return True
    print(Fore.YELLOW + "Подано", len(command) - 1,
          "аргументов, ожидалось:", arg_num)
    return False


def exit_cmd():
    """ Завершает выполнение программы. """
    sys.exit()


def help_cmd(*args):
    """ Выводит список всех команд сервиса/описание заданной команды (при
    поданном аргументе).

    help [%command%]

        %command% - команда для получения справки.
    """
