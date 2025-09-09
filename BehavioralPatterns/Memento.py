from __future__ import annotations
from abc import ABC, abstractmethod
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

    @abstractmethod
    def machine_ordinator(self) -> Machine:
        pass

    @abstractmethod
    def restore_state(self, memento: Machine) -> Machine:
        pass

@dataclass
class MachineMemento:
    state: Machine

@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"

    def machine_ordinator(self) -> Car:
        return Car(
            name=self.name,
            engine=self.engine,
            gearbox=self.gearbox,
            wheel=self.wheel,
            status=self.status,
            color = self.color
        )

    def restore_state(self, memento: Machine) -> None:
        self.engine = memento.engine
        self.gearbox = memento.gearbox
        self.wheel = memento.wheel
        self.color = memento.color
        self.status = memento.status

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"

    def machine_ordinator(self) -> Train:
        return Train(
            name=self.name,
            engine=self.engine,
            wheel=self.wheel,
            status=self.status,
            color = self.color
        )

    def restore_state(self, memento: Machine) -> None:
        self.engine = memento.engine
        self.wheel = memento.wheel
        self.color = memento.color
        self.status = memento.status


@dataclass
class Boat(Machine):
    name: str = "Boat"
    status: str = "New"

    def machine_ordinator(self) -> Boat:
        return Boat(
            name=self.name,
            engine=self.engine,
            gearbox=self.gearbox,
            status=self.status,
            color = self.color
        )

    def restore_state(self, memento: Machine) -> None:
        self.engine = memento.engine
        self.gearbox = memento.gearbox
        self.color = memento.color
        self.status = memento.status


class MachineHistory:
    def __init__(self):
        self._history: list[MachineMemento] = []

    def save(self, machine: Machine) -> None:
        self._history.append(MachineMemento(state=machine.machine_ordinator()))

    def undo(self, machine: Machine) -> None:
        if not self._history:
            return
        memento = self._history.pop()
        machine.restore_state(memento.state)


def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=4, color="red")
    history = MachineHistory()

    print(f"Initial: {car.get_description()}, status={car.get_status()}")

    history.save(car)

    car.color = "blue"
    car.wheel = 2
    car.status = "In repair"
    print(f"Modified: {car.get_description()}, status={car.get_status()}")

    history.undo(car)
    print(f"Restored: {car.get_description()}, status={car.get_status()}")


if __name__ == "__main__":
    main()
