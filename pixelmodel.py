"""
The PixelModel is responsible for controlling all the pixels in the entire
display, knowing each of their logical positions.
"""
class PixelModel (object):
    def __init__(self):
        self.pixelgroupcontrollers = [] # type: List[PixelGroupControllerInterface]
    def add_pixel_group_controller(self, controller):
        self.pixelgroupcontrollers.append(controller)
