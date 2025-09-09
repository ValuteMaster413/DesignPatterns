from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, machine: Machine) -> None:
        pass

class NewState(State):
    def handle(self, machine: Machine) -> None:
        print(f"{machine.name} is new and waiting for service.")
        machine._state = ReadyState()

    def __str__(self):
        return "New"

class ReadyState(State):
    def handle(self, machine: Machine) -> None:
        print(f"{machine.name} is ready and can be used.")

    def __str__(self):
        return "Ready"

class BrokenState(State):
    def handle(self, machine: Machine) -> None:
        print(f"{machine.name} is broken and needs repair.")
        machine._state = InServiceState()

    def __str__(self):
        return "Broken"

class InServiceState(State):
    def handle(self, machine: Machine) -> None:
        print(f"{machine.name} is in service.")
        machine._state = ReadyState()

    def __str__(self):
        return "InService"


class Machine(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._state: State = NewState()

    def get_status(self) -> str:
        return self._state.__str__()

    def request(self) -> None:
        self._state.handle(self)

class Car(Machine):
    def __init__(self):
        super().__init__(name="Car")

class Train(Machine):
    def __init__(self):
        super().__init__(name="Train")

class Boat(Machine):
    def __init__(self):
        super().__init__(name="Boat")

def main() -> None:
    car = Car()
    print(car.get_status())
    car.request()
    print(car.get_status())
    car.request()


if __name__ == "__main__":
    main()
