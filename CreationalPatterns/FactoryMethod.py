from abc import ABC, abstractmethod

class Machine(ABC):
    type = None
    status = "notReady"

    def __str__(self):
        return self.type

    @abstractmethod
    def honk(self):
        pass

    def status_changing(self):
        if self.status == "ready":
            self.status = "notReady"
        elif self.status == "notReady":
            self.status = "ready"
        else:
            return "status error"

        return self.status

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


def main():
    factory = CarFactory()

    transport = factory.create_machine()

    print(transport.status)
    transport.status_changing()
    print(transport.status)

    transport.honk()

if __name__ == "__main__":
    main()