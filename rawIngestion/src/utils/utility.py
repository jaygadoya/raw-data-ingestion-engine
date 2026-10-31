from pathlib import Path


def get_file_list_from_path(file_path: str) -> list:
    directory = Path(file_path.replace("\\","/"))
    files = []
    for item in directory.iterdir():
        files.append(item)
    return files