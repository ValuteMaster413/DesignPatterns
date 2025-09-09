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

    def request_service(self, mediator: Mediator) -> None:
        mediator.notify(self, "needs_service")

    def complete_check(self, mediator: Mediator) -> None:
        mediator.notify(self, "checked")

@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"


class Mediator(ABC):
    def __init__(self):
        self.machines: list[Machine] = []

    def add_machine(self, machine: Machine) -> None:
        self.machines.append(machine)

    @abstractmethod
    def notify(self, sender: Machine, event: str) -> None:
        pass


class MaintenanceMediator(Mediator):
    def notify(self, sender: Machine, event: str) -> None:
        if event == "needs_service":
            if sender.wheel is None or sender.wheel < 4:
                sender.status = "Send to wheel check"
            elif sender.engine is None or sender.engine == "":
                sender.status = "Send to engine check"
            elif sender.gearbox not in ["manual", "automatic"]:
                sender.status = "Send to gearbox check"
            else:
                sender.status = "Ready"
        elif event == "checked":
            sender.status = "Checked"


def main() -> None:
    mediator = MaintenanceMediator()

    car = Car(engine="1.6L", gearbox="manual", wheel=2, color="red")
    train = Train(gearbox="manual", wheel=8)

    mediator.add_machine(car)
    mediator.add_machine(train)

    car.request_service(mediator)
    train.request_service(mediator)

    for m in mediator.machines:
        print(f"{m.name} status: {m.get_status()}")

    car.complete_check(mediator)
    print(f"{car.name} final status: {car.get_status()}")

if __name__ == "__main__":
    main()
