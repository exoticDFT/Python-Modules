import os

def load_file(file_name, state="r"):
    try:
        f = open(file_name, state)
        return f
    except FileNotFoundError:
        print("Error reading file. Did you specify the correct file and path?")
        quit()


def change_dir(path):
    pass

