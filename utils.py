from config import FILE_CATEGORIES


def get_category(filename):
    extension = filename.lower().rsplit(".", 1)[-1]

    extension = "." + extension

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"