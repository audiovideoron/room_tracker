import webbrowser
import os


def display_in_browser(file_path):
    """Open the specified file in the default web browser.

    :param file_path: A string representing the file path of the file to be opened.
    :return: None
    """
    webbrowser.open('file://' + os.path.realpath(file_path))
