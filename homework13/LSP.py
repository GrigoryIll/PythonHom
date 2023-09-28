class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def tires_check(self):
        return "tires is ok!"


class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        return "use your legs!"

    def tires_check(self):
        return "tires is ok!"


class VehicleWithEngine(Vehicle):
    def __init__(self, name, color, engine):
        super().__init__(name, color)
        self.engine = engine

    def tires_check(self):
        return "tires is ok!"

    def start_engine(self):
        return "engine started!"


class Car(VehicleWithEngine):
    def __init__(self, name, color, engine):
        super().__init__(name, color, engine)


class Bicycle(VehicleWithoutEngine):
    def __init__(self, name, color):
        super().__init__(name, color)


car1 = Car("Lada", "Grey", "v12")
bicycle1 = Bicycle("Circle", "Blue")
print(car1.tires_check())
print(bicycle1.get_name())
