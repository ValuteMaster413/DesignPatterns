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

class Detail(ABC):
    type = None
    purpose = None
    status = None

    def __str__(self):
        return self.type

class Wheel(Detail):
    type = "wheel"


class Engine(Detail):
    type = "engine"


class GearBox(Detail):
    type = "gearbox"


class TrainWheel(Wheel):
    purpose = "Train"
    status = "new"


class TrainEngine(Engine):
    purpose = "Train"
    status = "new"


class TrainGearBox(GearBox):
    purpose = "Train"
    status = "new"


class CarWheel(Wheel):
    purpose = "car"
    status = "new"


class CarEngine(Engine):
    purpose = "car"
    status = "new"


class CarGearBox(GearBox):
    purpose = "car"
    status = "new"


class BoatEngine(Engine):
    purpose = "Boat"
    status = "new"


class BoatGearBox(GearBox):
    purpose = "Boat"
    status = "new"


class MachinePartsFactory (ABC):
    @abstractmethod
    def create_wheel(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_gearbox(self):
        pass

class TrainPartFactory(MachinePartsFactory):
    def create_wheel(self):
        return TrainWheel()
    def create_engine(self):
        return TrainEngine()
    def create_gearbox(self):
        return TrainGearBox()

class CarPartFactory(MachinePartsFactory):
    def create_wheel(self):
        return CarWheel()
    def create_engine(self):
        return CarEngine()
    def create_gearbox(self):
        return CarGearBox()

class BoatPartFactory(MachinePartsFactory):
    def create_engine(self):
        return BoatEngine()
    def create_gearbox(self):
        return BoatGearBox()
    def create_wheel(self):
        return None


def main():
    factory = CarPartFactory()
    engine = factory.create_engine()
    wheel = factory.create_wheel()
    gearbox = factory.create_gearbox()

    print(f"{engine.type}, Purpose: {engine.purpose}, Status: {engine.status}")
    print(f"{wheel.type}, Purpose: {wheel.purpose}, Status: {wheel.status}")
    print(f"{gearbox.type}, Purpose: {gearbox.purpose}, Status: {gearbox.status}")


if __name__ == "__main__":
    main()
