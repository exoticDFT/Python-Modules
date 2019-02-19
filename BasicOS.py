import os
from string import Template
from termcolor import colored

def change_dir(dir_path, proceed=True):
    try:
        os.chdir(dir_path)
    except Exception:
        error_message = Template("The path ${path} does not exist.")
        print_warn(error_message.substitute(path=dir_path))
        if not proceed:
            exit_program()


def exit_program():
    print_error("Cannot continue reliably. Exiting the program.")
    quit()


def load_file(file_name, state="r", proceed=True):
    try:
        f = open(file_name, state)
        return f
    except FileNotFoundError:
        print_warn(
            "Error reading file. Did you specify the correct file and path?"
        )
        if not proceed:
            exit_program()


def print_error(msg):
    print(colored(msg, "red"))


def print_success(msg):
    print(colored(msg, "green"))


def print_warn(msg):
    print(colored(msg, "yellow"))


