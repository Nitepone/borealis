class FollowerInterface(object):
    pass

class SimpleStripFollower(object):
    def __init__(self, length: int):
        self.length = length
    def spin(self):
        """main loop"""
        import time
        time.sleep(5)
