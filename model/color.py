"""
representation of color rendered by a single pixel (lightblub)
"""
class ColorInterface (object):

    def serialize(self) -> bytearray:
        return bytearray()

    @classmethod
    def deserialize(cls, binary: bytearray):
        return cls()


class ColorRGB24(object):
    
    def __init__(self, r: int, g: int, b: int):
        """
        r, g, and b should all be in the range [0, 255]
        """
        self._r = r & 0xFF
        self._g = g & 0xFF
        self._b = b & 0xFF

    @property
    def gbr(self):
        # TODO reconsider this hack
        return ColorRGB24(self._g, self._b, self._r)

    def to_int32(self):
        return (self._r << 16) | (self._g << 8) | self._b

    def serialize(self) -> bytearray:
        return bytearray([self._r, self._g, self._b])

    @classmethod
    def deserialize(cls, raw: bytearray):
        assert len(raw) == 3
        return cls(raw[0], raw[1], raw[2])
