from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Machine(ABC):
    name: str = None
    engine: str = None
    gearbox: str = None
    wheel: int = None
    color: str = None

    def get_description(self) -> str:
        return f"{self.name}: engine={self.engine}, gearbox={self.gearbox}, wheels={self.wheel}, color={self.color}"

@dataclass
class Flyweight(Machine):
    engine: str = None
    gearbox: str = None
    wheel: int = None
    color: str = None

@dataclass
class CarInstance:
    shared_state: Flyweight
    serial_number: str
    owner: str
    status: str

    def get_status(self) -> str:
        return self.status


class FlyweightFactory:
    flyweights: dict[str, Flyweight] = {}

    def make_flyweight(self, engine: str, gearbox: str, wheel: int, color: str) -> Flyweight:
        key = f"{engine}_{gearbox}_{wheel}_{color}"
        if key not in FlyweightFactory.flyweights:
            self.flyweights[key] = Flyweight(engine, gearbox, wheel, color)
            return self.flyweights[key]
        else:
            return self.flyweights[key]


def main() -> None:
    factory = FlyweightFactory()

    shared1 = factory.make_flyweight(engine="1.6L", gearbox="manual", wheel=4, color="red")
    shared2 = factory.make_flyweight(engine="1.6L", gearbox="manual", wheel=4, color="red")

    car1 = CarInstance(shared_state=shared1, serial_number="A123", owner="Alice", status="Ready")
    car2 = CarInstance(shared_state=shared2, serial_number="B456", owner="Bob", status="In repair")

    print(f"{car1.serial_number} ({car1.owner}): {car1.shared_state.get_description()}, status={car1.get_status()}")
    print(f"{car2.serial_number} ({car2.owner}): {car2.shared_state.get_description()}, status={car2.get_status()}")


if __name__ == "__main__":
    main()

