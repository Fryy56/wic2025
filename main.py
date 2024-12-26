# Modules
from colorama import Fore
import cmd

while True: # Main input loop
    command = input(Fore.RESET + ">>> ")

    match command:
        case "exit":
            cmd.exit_cmd()
        case _:
            print(Fore.RED + "'", command, "' - не команда сервиса. Используйте `help` для списка команд.", sep='')