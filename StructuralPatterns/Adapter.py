from abc import ABC
from dataclasses import dataclass
from typing import Optional

@dataclass
class Machine(ABC):
    name: str = None
    engine: str = None
    gearbox: str = None
    wheel: str = None
    color: str = None
    status: str = None

    def get_status(self) -> str:
        return self.status

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

@dataclass
class OldTracktor:
    name: str = "Old tracktor"

    engine: str = None
    gearbox: str = None
    wheel: str = None
    color: str = None
    status: str = None

    condition: str = "really old"

    def get_condition(self) -> str:
        return self.condition

class OldTracktorAdapter(Machine):
    def __init__(self, old_tracktor: OldTracktor):
        self.old_tracktor = old_tracktor

    def get_status(self) -> str:
        return self.old_tracktor.get_condition()

    @property
    def name(self) -> str: return self.old_tracktor.name


def main() -> None:
    car = Car(status="Ready")
    train = Train(status="In repair")
    boat = Boat(status="Ready")

    old_tracktor = OldTracktor()
    tracktor_adapter = OldTracktorAdapter(old_tracktor)

    machines: list[Machine] = [car, train, boat, tracktor_adapter]

    for m in machines:
        print(f"{m.name}: {m.get_status()}")


if __name__ == "__main__":
    main()