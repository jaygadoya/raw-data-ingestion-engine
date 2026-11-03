from pathlib import Path


def get_file_list_from_path(file_path: str) -> list:
    directory = Path(file_path.replace("\\","/"))
    files = []
    for item in directory.iterdir():
        files.append(item)
    return files

def fileRead(file_path: str) -> str:
    file_path = Path(file_path)
    file_content = file_path.read_text(encoding="utf-8")
    return file_content