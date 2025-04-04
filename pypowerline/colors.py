""" colors.py """

from enum import Enum


class Color(Enum):
    BLACK = "black"
    GREY = "grey"
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    LIGHT_GREY = "light_grey"
    DARK_GREY = "dark_grey"
    LIGHT_RED = "light_red"
    LIGHT_GREEN = "light_green"
    LIGHT_YELLOW = "light_yellow"
    LIGHT_BLUE = "light_blue"
    LIGHT_MAGENTA = "light_magenta"
    LIGHT_CYAN = "light_cyan"
    WHITE = "white"


def cprint(_text: str, _foreground: Color, _background: Color, _attrs=None):
    pass
