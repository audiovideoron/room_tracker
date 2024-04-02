import webbrowser
import os


def display_in_browser(file_path):
    webbrowser.open('file://' + os.path.realpath(file_path))
