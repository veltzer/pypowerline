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
    "pydmt",
    "pymakehelper",
]
test_requires: list[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
