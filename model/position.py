class PositionInterface(object):
    pass

class Position3D(PositionInterface):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
