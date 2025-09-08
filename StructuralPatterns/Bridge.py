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

    def perform_check(self, system: "MaintenanceSystem") -> str:
        return system.check(self)

@dataclass
class Car(Machine):
    name: str = "Car"
    status: str = "New"

class MaintenanceSystem(ABC):

    @abstractmethod
    def check(self, machine: "Machine") -> str:
        pass

class SimpleMaintenance(MaintenanceSystem):
    def check(self, machine: "Machine") -> str:
        if machine.wheel >= 4:
            machine.status = "Checked"
        else:
            machine.status = "Not enough wheels"

        return f"Simple check: {machine.status}"

class AdvancedMaintenance(MaintenanceSystem):
    def check(self, machine: "Machine") -> str:
        if machine.wheel == 4 and machine.engine is not None:
            machine.status = "Checked"
        else:
            machine.status = "Not enough wheels and engine"

        return f"Advanced check: {machine.status}"


def main() -> None:
    car = Car(gearbox="manual", wheel=3, color="red", status="New")

    simple_check = SimpleMaintenance()
    advanced_check = AdvancedMaintenance()

    print(car.perform_check(simple_check))
    print(car.perform_check(advanced_check))

if __name__ == "__main__":
    main()
