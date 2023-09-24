from abc import ABC, abstractmethod

import os


class Segment(ABC):
    @abstractmethod
    def get_text(self):
        """ return the text of the segment """
    @abstractmethod
    def get_color(self):
        """ return the color of the segment """
    @abstractmethod
    def get_background_color(self):
        """ return the background color of the segment """
    @abstractmethod
    def get_icon(self):
        """ return the special character of the segment """


class SegmentCwd(Segment):
    def __init__(self, color):
        self.color = color

    def get_text(self):
        return os.getcwd()

    def get_color(self):
        return self.color
