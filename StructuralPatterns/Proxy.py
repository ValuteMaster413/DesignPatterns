from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

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

class CarProxy(Machine):
    _real_car: Optional[Car] = None

    def get_status(self) -> str:
        if self._real_car is None:
            self._real_car = Car()
            return self._real_car.get_status()
        else:
            return self._real_car.get_status()

    def get_description(self) -> str:
        if self._real_car is None:
            self._real_car = Car()
            return self._real_car.get_description()
        else:
            return self._real_car.get_description()

def main() -> None:
    proxy_car = CarProxy()

    status = proxy_car.get_status()
    print(f"Car status: {status}")

    description = proxy_car.get_description()
    print(f"Car description: {description}")

if __name__ == "__main__":
    main()