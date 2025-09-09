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

@dataclass
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass

class ColorChanger(Command):
    def __init__(self, machine: Machine, new_color: str):
        self.machine = machine
        self.new_color = new_color
        self.old_color = None

    def execute(self) -> None:
        self.old_color = self.machine.color
        self.machine.color = self.new_color

        print("Set new color=", self.new_color)

    def undo(self) -> None:
        self.machine.color = self.old_color

        print("Set old color=", self.new_color)

class EngineChanger(Command):
    def __init__(self, machine: Machine, new_engine: str):
        self.machine = machine
        self.new_engine = new_engine
        self.old_engine = None

    def execute(self) -> None:
        self.old_engine = self.machine.engine
        self.machine.engine = self.new_engine

        print("Set new engine=", self.new_engine)

    def undo(self) -> None:
        self.machine.engine = self.old_engine

        print("Set old engine=", self.old_engine)

class GearBoxChanger(Command):
    def __init__(self, machine: Machine, new_gearbox: str):
        self.machine = machine
        self.new_gearbox = new_gearbox
        self.old_gearbox = None

    def execute(self) -> None:
        self.old_gearbox = self.machine.gearbox
        self.machine.gearbox = self.new_gearbox

        print("Set new gearbox=", self.new_gearbox)

    def undo(self) -> None:
        self.machine.gearbox = self.old_gearbox

        print("Set old gearbox=", self.new_gearbox)


class MachineController:
    def __init__(self):
        self.history: list[Command] = []

    def run_command(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

    def undo_last(self) -> None:
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


def main() -> None:
    car = Car(engine="1.6L", gearbox="manual", wheel=2, color="red", status="New")

    print(car.get_description())

    controller = MachineController()

    controller.run_command(ColorChanger(car, "blue"))
    controller.run_command(EngineChanger(car, "2.0L"))

    print(car.get_description())

    controller.undo_last()

    print(car.get_description())

if __name__ == "__main__":
    main()