""" utils.py """


def execute_python_file(file_path: str, vals=None):
    try:
        with open(file_path) as file:
            python_code = file.read()
            # pylint: disable=exec-used
            exec(python_code, globals(), vals)  # noqa: S102 - executing the user's config file is the point
    except FileNotFoundError:
        print(f"Error: The file [{file_path}] does not exist.")
