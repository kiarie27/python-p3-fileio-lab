from pathlib import Path

def _ensure_txt_path(file_name):
    """
    Return a Path object that points to <file_name>.txt.
    Accepts either a pathlib.Path or str for *file_name*. If the provided
    path already ends with ".txt", it is returned unchanged; otherwise
    ".txt" is appended to the string form of the path.
    """
    path = Path(file_name) if not isinstance(file_name, Path) else file_name
    if path.suffix != ".txt":
        path = Path(f"{path}.txt")
    return path

def write_file(file_name, file_content):
    """
    Create (or overwrite) <file_name>.txt and write *file_content* exactly.
    """
    path = _ensure_txt_path(file_name)
    with path.open("w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """
    Append *append_content* verbatim to <file_name>.txt.
    """
    path = _ensure_txt_path(file_name)
    with path.open("a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name):
    """
    Return the full contents of <file_name>.txt as a string.
    """
    path = _ensure_txt_path(file_name)
    with path.open("r", encoding="utf-8") as f:
        return f.read()
