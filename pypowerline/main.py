"""
main
"""
import os
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch

from termcolor import cprint

from pypowerline.static import DESCRIPTION, APP_NAME, VERSION_STR


symbols = {
    'detached': '\u2693',
    'ahead': '\u2B06',
    'behind': '\u2B07',
    'staged': '\u2714',
    'changed': '\u270E',
    'new': '?',
    'conflicted': '\u273C',
    'stash': '\u2398',
    'git': '\uE0A0',
    'hg': '\u263F',
    'bzr': '\u2B61\u20DF',
    'fossil': '\u2332',
    'svn': '\u2446',
    'separator': '\u25B6',
    'separator_b': '\uE0B0',
    'separator_thin': '\u276F',
    'separator_thin_b': '\uE0B1',
    'lock': '\uE0A2',
}


@register_endpoint(
    configs=[],
    description="do bash",
)
def bash() -> None:
    cwd = os.getcwd()
    # print(f"{cwd} > ", end="")
    cprint(f"{cwd}", "black", "on_light_magenta", end="")
    cprint(f"{symbols['separator_b']}", "light_cyan", "on_black", end="")


@register_endpoint(
    configs=[],
    description="do tmux",
)
def tmux() -> None:
    cwd = os.getcwd()
    print(f"{cwd} > ", end="")
    cprint(f"{cwd}", "red", "on_light_magenta", end="")


@register_endpoint(
    configs=[],
    description="print special symbols (used for development)",
)
def dump_symbols() -> None:
    for k, v in symbols.items():
        print(k, v)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
