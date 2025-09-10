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

@dataclass
class Train(Machine):
    name: str = "Train"
    status: str = "New"

@dataclass
class Boat(Machine):
    name: str = "Boat"
    status: str = "New"

class MachinePreparation(ABC):

    def prepare_machine(self, machine: Machine) -> None:
        self.check_engine(machine)
        self.check_gearbox(machine)
        self.check_wheel(machine)
        self.finalize_check(machine)

    @staticmethod
    def check_engine(machine: Machine) -> None:
        if machine.engine:
            print(f"{machine.name}: Engine OK")
        else:
            print(f"{machine.name}: Engine missing")

    @staticmethod
    def check_gearbox(machine: Machine) -> None:
        if hasattr(machine, 'gearbox') and machine.gearbox in ["manual", "automatic"]:
            print(f"{machine.name}: Gearbox OK")
        elif hasattr(machine, 'gearbox'):
            print(f"{machine.name}: Gearbox invalid")

    @staticmethod
    def check_wheel(machine: Machine) -> None:
        min_wheels = getattr(machine, "min_wheels", 4)
        if machine.wheel >= min_wheels:
            print(f"{machine.name}: Wheels OK")
        else:
            print(f"{machine.name}: Not enough wheels")

    @staticmethod
    def finalize_check(machine: Machine) -> None:
        machine.status = "Ready"

class CarPreparation(MachinePreparation):
    pass

class TrainPreparation(MachinePreparation):

    def check_engine(self, machine: Machine) -> None:
        pass

    def check_wheel(self, machine: Machine) -> None:
        min_wheels = 8
        if machine.wheel >= min_wheels:
            print(f"{machine.name}: Wheels OK")
        else:
            print(f"{machine.name}: Not enough wheels")


class BoatPreparation(MachinePreparation):
    def check_wheel(self, machine: Machine) -> None:
        if machine.wheel > 0:
            print(f"{machine.name}: Too many wheels???")
        else:
            print(f"{machine.name}: No wheels")

def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=4, color="red")
    train = Train(engine="V12", wheel=6, color="blue")
    boat = Boat(engine="Diesel", wheel=0, color="white")

    print("=== Car Preparation ===")
    car_prep = CarPreparation()
    car_prep.prepare_machine(car)
    print(f"Car status: {car.get_status()}\n")

    print("=== Train Preparation ===")
    train_prep = TrainPreparation()
    train_prep.prepare_machine(train)
    print(f"Train status: {train.get_status()}\n")

    print("=== Boat Preparation ===")
    boat_prep = BoatPreparation()
    boat_prep.prepare_machine(boat)
    print(f"Boat status: {boat.get_status()}\n")

if __name__ == "__main__":
    main()
