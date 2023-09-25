from abc import ABC, abstractmethod
import random


class Chest(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldChest(Chest):
    def open(self):
        return "Gold"


class SilverChest(Chest):
    def open(self):
        return "Silver"


class BronzeChest(Chest):
    def open(self):
        return "Bronze"


class ChestFactory:
    def create_chest(self, chests_list):
        self.chests_list = chests_list
        return random.choice(self.chests_list)


chest_list1 = [GoldChest(), BronzeChest(), SilverChest()]
factory = ChestFactory()

chest1 = factory.create_chest(chest_list1)
chest2 = factory.create_chest(chest_list1)
chest3 = factory.create_chest(chest_list1)
print(chest1.open(), chest2.open(), chest3.open())
