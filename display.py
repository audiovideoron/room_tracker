import webbrowser
from pathlib import Path


def display_in_browser(file_path):
    try:
        # Ensure file_path is a Path object
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        # Use as_uri() for file URLs, which handles special characters and is cleaner
        url_path = file_path.resolve().as_uri()

        webbrowser.open(url_path)
    except Exception as e:
        print(f"Error opening the browser: {e}")
