from typing import List


console_scripts: List[str] = [
    "pypowerline=pypowerline.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
]
make_requires: List[str] = [
    "pymakehelper",
    "pyclassifiers",
    "pydmt",
]
install_requires: List[str] = [
    "pytconf",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
