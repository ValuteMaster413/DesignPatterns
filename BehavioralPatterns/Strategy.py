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


@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"
    strategy: DrivingStrategy = None

    def perform_drive(self) -> str:
        if self.strategy:
            return self.strategy.drive(self)
        return "No strategy assigned"

class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self, car: Car) -> str:
        pass

class DriveFast(DrivingStrategy):
    def drive(self, car: Car) -> str:
        return "Driving fast"

class DriveSlow(DrivingStrategy):
    def drive(self, car: Car) -> str:
        return "Driving slow"

class DriveEconomically(DrivingStrategy):
    def drive(self, car: Car) -> str:
        return "Driving economically"

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=3, color="red")
    car.strategy = DriveFast()
    print(car.perform_drive())

    car.strategy = DriveEconomically()
    print(car.perform_drive())


if __name__ == "__main__":
    main()