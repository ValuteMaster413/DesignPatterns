from abc import ABC, abstractmethod

class Machine(ABC):
    type = None

    def __str__(self):
        return self.type

    @abstractmethod
    def honk(self):
        pass

class Train(Machine):
    type = "train"

    def honk(self):
        print("choo-choo")

class Car(Machine):
    type = "car"

    def honk(self):
        print("beep-beep")

class Boat(Machine):
    type = "boat"

    def honk(self):
        print("ahooga")

class MachineFactory(ABC):
    @abstractmethod
    def create_machine(self):
        pass

class TrainFactory(MachineFactory):
    def create_machine(self):
        train = Train()

        return train

class CarFactory(MachineFactory):
    def create_machine(self):
        car = Car()

        return car

class BoatFactory(MachineFactory):
    def create_machine(self):
        boat = Boat()

        return boat

