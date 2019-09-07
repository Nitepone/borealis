"""
The spacial model is a mapping from a 4D space to a colorspace.
"""
from .color import ColorInterface, ColorRGB24


class Spacial(object):
    def render(self, position: Position, time: float) -> ColorInterface:
        return ColorRGB24(1,2,3)
