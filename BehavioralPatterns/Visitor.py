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

    def accept(self, visitor: MaintenanceVisitor) -> None:
        visitor.visit_car(self)

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"

    def accept(self, visitor: MaintenanceVisitor) -> None:
        visitor.visit_train(self)

@dataclass
class Boat(Machine):
    name: str = "Boat"
    status: str = "New"

    def accept(self, visitor: MaintenanceVisitor) -> None:
        visitor.visit_boat(self)


class MaintenanceVisitor:
    def __init__(self):
        self.report = []

    def visit_car(self, car: Car) -> None:

        if car.gearbox is not None and car.gearbox in ["manual", "automatic"]:
            self.report.append("Gearbox OK")
        else:
            self.report.append("Gearbox invalid")

        if car.wheel >= 4:
            self.report.append("Wheels OK")
        else:
            self.report.append("Not enough wheels")

        if car.engine is not None and car.engine != "":
            self.report.append("Engine OK")
        else:
            self.report.append("Engine missing")

    def visit_train(self, train: Train) -> None:

        if train.wheel >= 8:
            self.report.append("Wheels OK")
        else:
            self.report.append("Not enough wheels")

        if train.engine is not None and train.engine != "":
            self.report.append("Engine OK")
        else:
            self.report.append("Engine missing")

    def visit_boat(self, boat: Boat) -> None:

        if boat.gearbox is not None and boat.gearbox in ["manual", "automatic"]:
            self.report.append("Gearbox OK")
        else:
            self.report.append("Gearbox invalid")

        if boat.wheel > 0:
            self.report.append("Too many wheels???")
        else:
            self.report.append("No wheels")

        if boat.engine is not None and boat.engine != "":
            self.report.append("Engine OK")
        else:
            self.report.append("Engine missing")

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=4)
    train = Train(engine="3.0L", wheel=8)
    boat = Boat(engine="1.0L", wheel=0)

    visitor = MaintenanceVisitor()

    for machine in [car, train, boat]:
        machine.accept(visitor)

    print(visitor.report)

if __name__ == "__main__":
    main()
