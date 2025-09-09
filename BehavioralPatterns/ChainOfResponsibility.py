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


@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"


class Handler(ABC):
    def __init__(self):
        self.next_handler: Handler | None = None

    def set_next_handler(self, handler: Handler) -> Handler:
        self.next_handler = handler
        return self

    @abstractmethod
    def handle(self, car: Car) -> list[str]:
        pass

class EngineCheck(Handler):
    def handle(self, car: Car) -> list[str]:
        report = []

        if car.engine is not None and car.engine != "":
            report.append("Engine OK")
        else:
            report.append("Engine missing")

        if self.next_handler:
            report.extend(self.next_handler.handle(car))

        return report

class WheelsCheck(Handler):
    def handle(self, car: Car) -> list[str]:
        report = []

        if car.wheel >= 4:
            report.append("Wheels OK")
        else:
            report.append("Not enough wheels")

        if self.next_handler:
            report.extend(self.next_handler.handle(car))

        return report

class GearboxCheck(Handler):
    def handle(self, car: Car) -> list[str]:
        report = []

        if car.gearbox is not None and car.gearbox in ["manual", "automatic"]:
            report.append("Gearbox OK")
        else:
            report.append("Gearbox invalid")

        if self.next_handler:
            report.extend(self.next_handler.handle(car))

        return report

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=2, color="red", status="New")
    engine = EngineCheck()
    wheels = WheelsCheck()
    gearbox = GearboxCheck()

    engine.set_next_handler(wheels.set_next_handler(gearbox))

    report = engine.handle(car)
    print(report)

if __name__ == "__main__":
    main()