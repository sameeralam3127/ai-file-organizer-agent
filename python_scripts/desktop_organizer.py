from pathlib import Path
from config import FILE_CATEGORIES
from file_utils import move_file

desktop = Path.home() / "Desktop"


def organize_desktop():

    moved_files = 0

    for file in desktop.iterdir():

        if file.is_file():

            ext = file.suffix.lower()

            for folder, extensions in FILE_CATEGORIES.items():

                if ext in extensions:
                    result = move_file(file, folder)
                    print(result)
                    moved_files += 1
                    break

    if moved_files == 0:
        print("Desktop already organized.")


if __name__ == "__main__":
    organize_desktop()