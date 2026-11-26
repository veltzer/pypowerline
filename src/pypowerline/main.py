"""
main
"""
import os
from typing import TYPE_CHECKING, Any

from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pypowerline.colors import Color, cprint
from pypowerline.static import APP_NAME, DESCRIPTION, VERSION_STR
from pypowerline.symbols import Symbol
from pypowerline.utils import execute_python_file

if TYPE_CHECKING:
    from pypowerline.segments import Segment

# What a user's segments.py can realistically raise while being executed.
USER_CONFIG_ERRORS = (
    ArithmeticError,
    AttributeError,
    ImportError,
    LookupError,
    NameError,
    OSError,
    RuntimeError,
    SyntaxError,
    TypeError,
    ValueError,
)


@register_endpoint(
    configs=[],
    description="print the location of pypowerlines config file",
)
def print_config_file() -> None:
    print(os.path.expanduser("~/.config/pypowerline/segments.py"))


@register_endpoint(
    configs=[],
    description="print a prompt for bash",
)
def bash() -> None:
    py_file = os.path.expanduser("~/.config/pypowerline/segments.py")
    vals: dict[str, Any] = {}
    try:
        execute_python_file(py_file, vals=vals)
    except USER_CONFIG_ERRORS as e:
        print(e)
        print("cannot execute segments > ", end="")
        return
    if "segments" not in vals:
        print("segments not defined > ", end="")
        return
    segments: list[Segment] = vals["segments"]
    for segment in segments:
        text = ""
        if segment.icon is not None:
            # two spaces after the icon; why two is not known (doc/TOFIX.md)
            text += segment.icon.value + "  "
        text += segment.get_text()
        if segment.color is None or segment.background is None:
            print(text, end="")
        else:
            cprint(
                text,
                segment.color,
                segment.background,
            )
        if segment.separator is not None:
            text = segment.separator.value
            if segment.color is None or segment.background is None:
                print(text, end="")
            else:
                attrs: list[str] = []
                if segment.reverse_sep:
                    attrs.append("reverse")
                    attrs.append("reset")
                cprint(
                    text,
                    segment.color,
                    segment.background,
                    _attrs=attrs,
                )


@register_endpoint(
    configs=[],
    description="do some test printing on the terminal (development purposes)",
)
def test() -> None:
    cwd = os.getcwd()
    symbol = Symbol.SEPARATOR_B.value
    print(f"{cwd} > ", end="")
    cprint("cwd", Color.BLACK, Color.LIGHT_MAGENTA)
    cprint("cwd", Color.BLACK, Color.LIGHT_GREY)
    cprint("cwd", Color.BLACK, Color.GREY)
    cprint("cwd", Color.BLACK, Color.BLUE)
    cprint("cwd", Color.BLACK, Color.LIGHT_BLUE)
    cprint("cwd", Color.WHITE, Color.CYAN)
    cprint("cwd", Color.WHITE, Color.GREEN)
    cprint(f"{symbol}", Color.LIGHT_CYAN, Color.BLACK)
    print()


@register_endpoint(
    configs=[],
    description="do tmux",
)
def tmux() -> None:
    cwd = os.getcwd()
    print(f"{cwd} > ", end="")
    cprint(f"{cwd}", Color.RED, Color.LIGHT_MAGENTA)


@register_endpoint(
    configs=[],
    description="print special symbols (used for development)",
)
def dump_symbols() -> None:
    for symbol in Symbol:
        print(symbol, symbol.value)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
