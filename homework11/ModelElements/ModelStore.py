from IModelChanger import *
from IModelChangedObserver import *
from InMemoryModel import PoligonalModel
from InMemoryModel import Scene
from InMemoryModel import Flash
from InMemoryModel import Camera


class ModelStore(IModelChanger):
    def __init__(self):
        self.models = [PoligonalModel()]
        self.scenes = [Scene()]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self._changeObservers = changeObservers

    def getScene(self, index):
        return self.scenes[index]

    def NotifyChange(self, sender):
        self.sender = sender


full_model = ModelStore()
full_model.models.append(models)
full_model.scenes.append(scenes)
full_model.flashes.append(flashes)
full_model.cameras.append(cameras)
