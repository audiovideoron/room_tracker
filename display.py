# In display.py
import webbrowser
from pathlib import Path


def display_html_file(month_dir: Path, month: str):
    """
    Displays an HTML file in the browser.
    """
    html_file_path = month_dir / f'{month}_calendar.html'
    webbrowser.open(str(html_file_path), new=2)  # new=2 opens in a new tab
