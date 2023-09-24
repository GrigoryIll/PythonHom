from PoligonalModel import *
from PoligonalModel import *
from PoligonalModel import *


class Scene:

    def __init__(self, id, models, cameras):
        self.id = id
        if len(models) < 1:
            raise Exception("Должен быть хотя бы один model!")
        else:
            self.models = models
        if len(cameras) < 1:
            raise Exception("Должен быть хотя бы один camera!")
        else:
            self.cameras = cameras
        self.flashes = flashes

    def method1(self, type1):
        return type1

    def method2(self, type1, type2):
        return type1
