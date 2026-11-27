""" segments.py """

import os
import os.path
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from pypowerline.symbols import Symbol

if TYPE_CHECKING:
    from pypowerline.colors import Color


class Segment(ABC):
    def __init__(
            self,
            color: Color | None = None,
            background: Color | None = None,
            icon: Symbol | None = None,
            separator: Symbol | None = Symbol.SEPARATOR,
            *,
            reverse_sep: bool = True,
    ) -> None:
        self.color = color
        self.background = background
        self.icon = icon
        self.separator = separator
        self.reverse_sep = reverse_sep

    @abstractmethod
    def get_text(self) -> str:
        """ return the text of the segment """


class SegmentCwd(Segment):
    def __init__(
            self,
            color: Color | None = None,
            background: Color | None = None,
            icon: Symbol | None = Symbol.FOLDER,
            separator: Symbol | None = Symbol.SEPARATOR_B,
            *,
            reverse_sep: bool = True,
            last_only: bool = False,
            home_as_tilde: bool = True,
    ) -> None:
        super().__init__(
            color=color,
            background=background,
            icon=icon,
            separator=separator,
            reverse_sep=reverse_sep,
        )
        self.last_only = last_only
        self.home_as_tilde = home_as_tilde
        self.home_directory = os.path.expanduser("~")

    def get_text(self) -> str:
        cwd = os.getcwd()
        if self.home_as_tilde and cwd.startswith(self.home_directory):
            cwd = "~" + cwd[len(self.home_directory):]
        if self.last_only:
            return os.path.basename(cwd)
        return cwd


class SegmentForward(Segment):
    def __init__(self) -> None:
        super().__init__()

    def get_text(self) -> str:
        return " > "


class SegmentSpace(Segment):
    def __init__(self) -> None:
        super().__init__(separator=None)

    def get_text(self) -> str:
        return " "
