from abc import ABC, abstractmethod


class Machine(ABC):
    name = None
    engine = None
    gearbox = None
    wheel = None
    color = None
    status = None


class Car(Machine):
    name = "Car"
    status = "New"

class Train(Machine):
    name = "Train"
    status = "New"

class Boat(Machine):
    name = "Boat"
    status = "New"


class MachineBuilder(ABC):

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_gearbox(self, gearbox):
        pass

    @abstractmethod
    def set_wheel(self, wheel):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(MachineBuilder):

    def __init__(self):
        self.machine = Car()

    def set_engine(self, engine):
        self.machine.engine = engine

        return self

    def set_gearbox(self, gearbox):
        self.machine.gearbox = gearbox

        return self

    def set_wheel(self, wheel):
        self.machine.wheel = wheel

        return self

    def set_color(self, color):
        self.machine.color = color

        return self

    def get_result(self):
        return self.machine


class TrainBuilder(MachineBuilder):

    def __init__(self):
        self.machine = Train()

    def set_engine(self, engine):
        self.machine.engine = engine

        return self

    def set_gearbox(self, gearbox):
        return self

    def set_wheel(self, wheel):
        self.machine.wheel = wheel

        return self

    def set_color(self, color):
        self.machine.color = color

        return self

    def get_result(self):
        return self.machine


class BoatBuilder(MachineBuilder):

    def __init__(self):
        self.machine = Boat()

    def set_engine(self, engine):
        self.machine.engine = engine

        return self

    def set_gearbox(self, gearbox):
        self.machine.gearbox = gearbox

        return self

    def set_wheel(self, wheel):
        return self

    def set_color(self, color):
        self.machine.color = color

        return self

    def get_result(self):
        return self.machine


class Director:

    @staticmethod
    def build_default_car():
        car_builder = CarBuilder()
        default_car = car_builder.set_engine("1.6L").set_gearbox("manual").set_wheel(4).set_color("red").get_result()
        return default_car

    @staticmethod
    def build_default_train():
        train_builder = TrainBuilder()
        default_train = train_builder.set_engine("diesel").set_wheel(8).set_color("diesel").get_result()
        return default_train

    @staticmethod
    def build_default_boat():
        boat_builder = BoatBuilder()
        default_boat = boat_builder.set_engine("100HP").set_gearbox("manual").set_color("yellow").get_result()
        return default_boat


def main():
    default_car = Director.build_default_car()
    default_train = Director.build_default_train()
    default_boat = Director.build_default_boat()

    print(
        f"Name: {default_car.name}, Engine: {default_car.engine}, Gearbox: {default_car.gearbox}, Wheel: {default_car.wheel}, Color: {default_car.color}, Status: {default_car.status}")
    print(
        f"Name: {default_train.name}, Engine: {default_train.engine}, Gearbox: {default_train.gearbox}, Wheel: {default_train.wheel}, Color: {default_train.color}, Status: {default_train.status}")
    print(
        f"Name: {default_boat.name}, Engine: {default_boat.engine}, Gearbox: {default_boat.gearbox}, Wheel: {default_boat.wheel}, Color: {default_boat.color}, Status: {default_boat.status}")


if __name__ == "__main__":
    main()