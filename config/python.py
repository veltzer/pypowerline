""" python deps for this project """

scripts: dict[str,str] = {
    "pypowerline": "pypowerline.main:main",
}

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pytest",
    "pylint",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
