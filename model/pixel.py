class Pixel(object):
    def __init__(self, identifier: int, position: Position):
        self._position = position
        self._id = identifier

class PixelGroup():
    def __init__(self, pixels: List[Pixel]):
        self._pixels = pixels
