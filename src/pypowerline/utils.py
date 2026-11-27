""" utils.py """

from typing import Any


def execute_python_file(file_path: str, vals: dict[str, Any] | None = None) -> None:
    try:
        with open(file_path) as file:
            python_code = file.read()
            exec(python_code, globals(), vals)  # executing the user's config file is the point
    except FileNotFoundError:
        print(f"Error: The file [{file_path}] does not exist.")
