from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Machine(ABC):

    def __init__ (self) -> None:
        self._observers: list[Observer] = []

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

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(self, event)

@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"
    engine: str = None
    gearbox: str = None
    wheel: int = None
    color: str = None

    def __post_init__(self):
        super().__init__()

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"
    engine: str = None
    wheel: int = None
    color: str = None

    def __post_init__(self):
        super().__init__()

@dataclass
class Boat(Machine):
    name: str = "Boat"
    status: str = "New"
    engine: str = None
    gearbox: str = None
    wheel: int = None
    color: str = None

    def __post_init__(self):
        super().__init__()

class Observer(ABC):
    @abstractmethod
    def update(self, machine: Machine, event: str) -> None:
        pass

class Garage(Observer):
    def update(self, machine: Machine, event: str) -> None:
        print(f"Garage notified: {machine.name} - {event}")

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=3, color="red")
    garage = Garage()

    car.add_observer(garage)
    car.status = "needs_service"
    car.notify("needs_service")


if __name__ == "__main__":
    main()


