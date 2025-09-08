from abc import ABC
from dataclasses import dataclass

@dataclass
class Machine(ABC):
    name: str = None
    engine: str = None
    gearbox: str = None
    wheel: int = None
    color: str = None
    status: str = None

    def get_status(self) -> str:
        return self.status

    def get_description(self) -> str:
        return f"{self.name}: engine={self.engine}, gearbox={self.gearbox}, wheels={self.wheel}, color={self.color}"

@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"

@dataclass
class Boat(Machine):
    name: str = "Boat"
    status: str = "New"


class MachineDecorator(ABC):
    def __init__(self, machine: Machine):
        self.machine = machine

    def get_description(self) -> str:
        return self.machine.get_description()

class GPSDecorator(MachineDecorator):

    def get_description(self) -> str:
        base_description = self.machine.get_description()
        return f"{base_description}, GPS: yes"

class ExtraWheelsDecorator(MachineDecorator):

    def __init__(self, machine: Machine, extra_wheels: int):
        super().__init__(machine)
        self.machine.wheel += extra_wheels

    def get_description(self) -> str:
        return self.machine.get_description()


def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=4, color="red")
    print(car.get_description())
    
    car_with_gps = GPSDecorator(car)
    print(car_with_gps.get_description())

    car_with_extra_wheels = ExtraWheelsDecorator(car, extra_wheels=2)
    print(car_with_extra_wheels.get_description())


if __name__ == "__main__":
    main()
