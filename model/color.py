"""
representation of color rendered by a single pixel (lightblub)
"""
class ColorInterface (object):

    def serialize(self) -> bytearray:
        return bytearray()

    @classmethod
    def deserialize(cls, binary: bytearray)
        return cls()

class ColorRGB24(object):
    
    def __init__(self, r: int, g: int, b: int):
        """
        r, g, and b should all be in the range [0, 255]
        """
        self._r = r & 0xFF
        self._g = g & 0xFF
        self._b = b & 0xFF

    def serialize(self) -> bytearray:
        return bytearray([self._r, self._g, self._b])

    @classmethod
    def deserialize(cls, raw: bytearray)
        assert len(raw) == 3
        return cls(raw[0], raw[1], raw[2])
