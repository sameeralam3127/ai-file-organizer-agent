from pathlib import Path
import shutil

desktop = Path.home() / "Desktop"


def scan_desktop():

    files = []

    for item in desktop.iterdir():

        # ignore hidden files like .DS_Store
        if item.is_file() and not item.name.startswith("."):
            files.append(item.name)

    return files


def create_folder(name):

    folder = desktop / name
    folder.mkdir(exist_ok=True)

    return f"Folder '{name}' ready"


def move_file(filename, folder):

    source = desktop / filename
    destination = desktop / folder

    destination.mkdir(exist_ok=True)

    target = destination / filename

    if not source.exists():
        return f"{filename} not found"

    if target.exists():
        return f"{filename} already organized"

    shutil.move(str(source), target)

    return f"{filename} moved to {folder}"