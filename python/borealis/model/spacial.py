"""
The spacial model is a mapping from a 4D space to a colorspace.
"""
from .color import ColorInterface, ColorRGB24
from .position import PositionInterface
from .pixel import Pixel


class Spacial(object):
    def render(self, pixel: Pixel, time: float) -> ColorInterface:
        return ColorRGB24((int(time) & 0xF) << 4, 0, int(pixel._position.project_normalized() * 255))

class SpacialTimeWheel(object):

    def render(self, _, time: float) -> ColorInterface:

        return ColorRGB24((int(time) & 0xF) << 4, 0, 0)
