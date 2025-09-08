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

    def check_engine(self) -> bool:
        if self.engine is not None and self.engine != "":
            return True
        else:
            return False

    def check_wheels(self) -> bool:
        if self.wheel >= 4:
            return True
        else:
            return False

    def check_gearbox(self) -> bool:
        if self.gearbox is not None and self.gearbox in ["manual", "automatic"]:
            return True
        else:
            return False

class Car(Machine):
    name: str = "Car"
    status: str = "New"

class CarPreparation:
    def __init__(self, car: Car):
        self.car = car
        self.report = []

    def prepare(self) -> str:
        if self.car.check_engine():
            self.report.append("Engine OK")
        else:
            self.report.append("Engine missing")

        if self.car.check_wheels():
            self.report.append("Wheels OK")
        else:
            self.report.append("Not enough wheels")

        if self.car.check_gearbox():
            self.report.append("Gearbox OK")
        else:
            self.report.append("Gearbox invalid")

        return ", ".join(self.report)

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=2, color="red", status="New")
    preparation = CarPreparation(car)
    report = preparation.prepare()
    print(f"Car preparation report: {report}")

if __name__ == "__main__":
    main()

