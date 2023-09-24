from Point3D import *
from Angle3D import *
from Color import *


class Flash:
    def __init__(self, location, angle, color, power):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle):
        pass

    def move(self, point):
        pass
