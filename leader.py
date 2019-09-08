import time

from follower import FollowerInterface
from model.color import ColorRGB24
from model.position import Position3D
from model.spacial import Spacial


class LeaderInterface(object):
    def register(self, Follower):
        pass


class LeaderTCPProxy(LeaderInterface):
    pass


class Leader(LeaderInterface):

    def __init__(self):
        self.followers = []
        self.spacial = Spacial()

    def register(self, follower: FollowerInterface):
        self.followers.append(follower)

    def update_follower(self, follower):
        for pixel in follower.pixel_iter():
            c = self.spacial.render(pixel, time.time())
            follower.update(pixel, c)
        follower.flush()

    def spin(self):
        i = 0
        while True:
            # c = s.render(None, time.time())
            # c = ColorRGB24(i, 0, 0)
            for f in self.followers:
                self.update_follower(f)
            time.sleep(0.1)
            i = (i + 2) % 255
