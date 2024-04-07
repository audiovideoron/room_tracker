import webbrowser
from urllib.parse import quote
import os


def display_in_browser(file_path):
    try:
        url_path = 'file://' + quote(os.path.realpath(file_path))
        webbrowser.open(url_path)
    except Exception as e:
        print(f"Error opening the browser: {e}")
