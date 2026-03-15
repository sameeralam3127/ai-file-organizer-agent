import shutil
from pathlib import Path

desktop = Path.home() / "Desktop"


def create_folder(folder_name):
    folder_path = desktop / folder_name
    folder_path.mkdir(exist_ok=True)
    return folder_path


def move_file(file_path, folder_name):
    target_folder = create_folder(folder_name)
    destination = target_folder / file_path.name

    if destination.exists():
        return f"Skipped {file_path.name} (already exists)"

    shutil.move(str(file_path), destination)
    return f"Moved {file_path.name} → {folder_name}"