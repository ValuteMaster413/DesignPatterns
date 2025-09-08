from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class CarComponent(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass

@dataclass
class Part(CarComponent):
    name: str
    price: int

    def get_description(self) -> str:
        return f"{self.name}"

    def get_price(self) -> int:
        return self.price


class CarComposite(CarComponent):

    def __init__(self):
        self.parts: list[CarComponent] = []

    def add_part(self, component: CarComponent) -> None:
        self.parts.append(component)

    def get_description(self) -> str:
        descriptions = []
        for part in self.parts:
            descriptions.append(part.get_description())
        return ", ".join(descriptions)

    def get_price(self) -> int:
        price = 0
        for part in self.parts:
            price += part.get_price()
        return price

def main() -> None:
    engine = Part("Engine V6", 5000)
    wheel1 = Part("Front Left Wheel", 800)
    wheel2 = Part("Front Right Wheel", 800)
    wheel3 = Part("Back Left Wheel", 800)
    wheel4 = Part("Back  Right Wheel", 800)
    seat = Part("Driver Seat", 300)


    car = CarComposite()
    car.add_part(engine)
    car.add_part(seat)

    wheelset = CarComposite()
    wheelset.add_part(wheel1)
    wheelset.add_part(wheel2)
    wheelset.add_part(wheel3)
    wheelset.add_part(wheel4)

    car.add_part(wheelset)

    print(car.get_description())
    print(car.get_price())


if __name__ == "__main__":
    main()