from abc import abstractmethod


class Vehicle:
    def __init__(self, company, model, year_release, num_wheels, speed):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = num_wheels
        self.speed = speed

    @abstractmethod
    def testDrive():
        pass

    @abstractmethod
    def park():
        pass


class Car(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=4, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def testDrive(self, speed=60):
        self.speed = speed

    def park(self, speed=0):
        self.speed = speed


car1 = Car("Toyota", "Camry", "2020")

# print(car1.speed)
car1.testDrive()
print(car1.speed)
# car1.park()
# print(car1.speed)
#


class Motocycle(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=2, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def testDrive(self, speed=75):
        self.speed = speed

    def park(self, speed=0):
        self.speed = speed


# motocycle1 = Motocycle("Ducatti", "Diavel", "2021")

# print(motocycle1.speed)
# motocycle1.testDrive()
# print(motocycle1.speed)
# motocycle1.park()
# print(motocycle1.speed)
