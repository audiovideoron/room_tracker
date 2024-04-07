from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
VISUALIZATIONS_DIR = BASE_DIR / 'visualizations'

if __name__ == "__main__":
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"VISUALIZATIONS_DIR: {VISUALIZATIONS_DIR}")
