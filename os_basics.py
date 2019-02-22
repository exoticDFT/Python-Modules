import custom_print as cprnt
import os
from string import Template

def change_dir(dir_path, proceed=True):
    """
    Changes the current working directory if the path exists.

    Parameters
    ----------
    dir_path : string
        The directory path in which you would like to make your current working
        directory.
    proceed : Boolean, optional
        A Boolean to let the program know whether to proceed or end on an
        error.

    Raises
    ------
    Exception
        If the directory path does not exist
    """
    try:
        os.chdir(dir_path)
    except Exception:
        error_message = Template("The path ${path} does not exist.")
        cprnt.print_warn(error_message.substitute(path=dir_path))
        if not proceed:
            exit_program()


def exit_program(**message):
    """
    Exits the program after displaying a message to the user.
    
    Parameters
    ----------
    message : dictionary, optional
        Dictionary containing the key 'msg' which has the message you'd like
        to be displayed instead of the default.
    """
    if ('msg' in message):
        cprnt.print_error(message['msg'])
    else:
        cprnt.print_error("Cannot continue reliably. Exiting the program.")
    quit()


def open_file(file_name, mode='r', proceed=True):
    """
    Open a file with specified mode of the file.

    Parameters
    ----------
    file_name : string
        Name of the file in which to return.
    mode : string, optional
        Mode is which the file should be opened. The value of mode should
        correspond to the expected characters used in the "open' function.
    proceed : Boolean, optional
        A Boolean to let the program know whether to proceed or end on an
        error.

    Returns
    -------
    f : _io.TextIOWrapper
        The file which is opened if no errors occur.

    Raises
    ------
    FileNotFoundError
        If the file is not found and cannot be opened.
    """
    try:
        f = open(file_name, mode)
        return f
    except FileNotFoundError:
        error_msg = Template(
            "There was a problem reading the file:\n${filename}"
        )
        cprnt.print_error(
            error_msg.substitute(filename=os.path.abspath(file_name))
        )
        if not proceed:
            exit_program()
