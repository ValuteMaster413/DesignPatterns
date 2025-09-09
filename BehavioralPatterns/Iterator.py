from __future__ import annotations
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


class Fleet:
    def __init__(self) -> None:
        self.machines: list[Machine] = []

    def __iter__(self) -> FleetIterator:
        return FleetIterator(self)

    def add_machine(self, machine: Machine) -> None:
        self.machines.append(machine)


class FleetIterator:
    def __init__(self, fleet: Fleet) -> None:
        self.fleet = fleet
        self.index = 0

    def __next__(self) -> Machine:
        if self.index >= len(self.fleet.machines):
            raise StopIteration
        machine = self.fleet.machines[self.index]
        self.index += 1
        return machine


def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=4, color="red")
    train = Train(engine="diesel", gearbox="manual", wheel=8, color="blue")
    boat = Boat(engine="100HP", gearbox="manual", wheel=0, color="yellow")

    fleet = Fleet()
    fleet.add_machine(car)
    fleet.add_machine(train)
    fleet.add_machine(boat)

    for machine in fleet:
        print(machine.get_description())


if __name__ == "__main__":
    main()