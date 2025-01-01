# Modules   pylint: disable=missing-module-docstring
import cmd
from colorama import init, Fore


init()   # Initialize colorama for color compatibility
while True:   # Main input loop
    command = input(Fore.RESET + ">>> ").split()
    command_header = command[0]
    match command_header:
        case "exit":
            if cmd.arg_test(0, command):
                cmd.exit_cmd()
        case _:
            print(Fore.RED + "'", command_header, "' - не команда сервиса. "
                  "Используйте `help` для списка команд.", sep='')
