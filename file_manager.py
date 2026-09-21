from pathlib import Path
import shutil

from utils import get_category


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist.")
        return

    if not folder.is_dir():
        print("The path is not a folder.")
        return

    for file in folder.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.name)

        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name

        shutil.move(str(file), str(destination))

        print(f"Moved: {file.name} → {category}/")