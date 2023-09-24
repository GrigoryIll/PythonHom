from abc import ABC, abstractmethod

class IModelChangeObserver(ABC):
    
    @abstractmethod
    def ApplyUpdateModel(self):
        pass