from termcolor import colored

def print_error(msg):
    """
    Prints the provided message in the color red to signify an error.

    Parameters
    ----------
    msg : string
        The message in which to display to the user.
    """
    print(colored(msg, "red"))


def print_success(msg):
    """
    Prints the provided message in the color green to signify success.

    Parameters
    ----------
    msg : string
        The message in which to display to the user.
    """
    print(colored(msg, "green"))


def print_warn(msg):
    """
    Prints the provided message in the color yellow to signify a warning.

    Parameters
    ----------
    msg : string
        The message in which to display to the user.
    """
    print(colored(msg, "yellow"))
