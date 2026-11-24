# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pypowerline/colors.py:26` - `cprint()` is an empty stub (`pass`) left behind when termcolor was removed (`doc/DONE.txt:1`). Every segment that has both `color` and `background` set goes through it in `bash()` (`src/pypowerline/main.py:51` and `main.py:65`), so its text and separator are silently dropped from the prompt, and the `test`/`tmux` endpoints print almost nothing. Implement it with ANSI escapes (mapping `Color` to SGR codes, honouring `reverse`/`reset` attrs and `end=""`), or bash prompt-safe `\[...\]` wrapped codes for the `bash` endpoint.

## Medium

- `src/pypowerline/create_color.py:27` - a development script lives inside the installed package and prints 240 "Color N: RGB(...)" lines at import time; `tests/unit_tests/test_basic.py:28` and sphinx autodoc (`sphinx/pypowerline.rst:26`) both import it. Its cube values are also wrong: xterm's 6x6x6 cube levels are 0, 95, 135, 175, 215, 255, not `r * 40` (line 17). Move it out of `src/` (or wrap it in a function / `if __name__ == "__main__":`) and fix the levels.
- `src/pypowerline/segments.py:57` - `cwd.startswith(self.home_directory)` is a plain string prefix test, so with HOME=`/home/mark` a cwd of `/home/markus/x` renders as `~us/x`. Check `cwd == home or cwd.startswith(home + os.sep)`.
- `src/pypowerline/configs.py:7` - `ConfigGeneral` (the `icons`/`colors` switches) is never referenced: every endpoint in `src/pypowerline/main.py` registers `configs=[]`, so the options cannot be set and are never consulted. Wire it into `bash()` or delete it.

## Low

- `src/pypowerline/utils.py:11` - a missing config file is reported with a print and then swallowed, so `bash()` additionally prints "segments not defined > " (`src/pypowerline/main.py:39`): two error strings land in the user's prompt. Let `FileNotFoundError` propagate to the existing handler in `bash()` (line 34) so one message is printed.
- `src/pypowerline/main.py:33` - `# pylint: disable=...` comments (also `src/pypowerline/segments.py:12`, `segments.py:33`, `src/pypowerline/utils.py:8`) are leftovers; pylint is not run here (ruff + mypy are). Remove them.
- `pyproject.toml:85` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist in this repo; reduce it to `src`.
- `doc/TODO.txt:1` - the file is empty (0 bytes); delete it or fill it.
