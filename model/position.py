# TODO this naming scheme is kinda an anti-pattern
class PositionInterface(object):

    def project(self) -> float:
        """project this position down to a single vector"""
        return 0.

    def project_normalized(self) -> float:
        """project this position down to a scalar in the range [0,1]"""
        return 0.


class Position3D(PositionInterface):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class PositionNormalized3D(PositionInterface):
    """Represents a 3-dimensional position where all coordinates are included
    in the range [0, 1]."""
    def __init__(self, x: float, y: float, z: float):
        self._x = x % 1
        self._y = y % 1
        self._z = z % 1
    
    def project_normalized(self) -> float:
        """Return a scalar in the range [0,1]"""
        return (self._x + self._y + self._z) / 3.

    def project(self) -> float:
        """Calculate the scalar vector projection of the 3D position vector
        onto the (1,1,1) vector"""
        return (self._x + self._y + self.z) * 0.5773502691896258
