"""
The spacial model is a mapping from a 4D space to a colorspace.
"""
from .color import ColorInterface, ColorRGB24
from .position import PositionInterface


class Spacial(object):
    def render(self, position: PositionInterface, time: float) -> ColorInterface:
        return ColorRGB24((int(time) & 0xF) << 4, 0, 0)
