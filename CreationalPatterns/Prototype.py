from abc import ABC, abstractmethod
import copy

class Machine(ABC):
    name = None
    engine = None
    gearbox = None
    wheel = None
    color = None
    status = None


class Car(Machine):
    name = "Car"
    engine = "1.6L"
    gearbox = "manual"
    wheel = 4
    color = "red"
    status = "New"

    def clone(self):
        car_clone = copy.deepcopy(self)
        return car_clone

    def __str__(self):
        return f"{self.name} {self.engine} {self.gearbox} {self.wheel} {self.color}"


def main():
    prototype_car = Car()

    car1 = prototype_car.clone()
    print(car1)

    car2 = prototype_car.clone()
    print(car2)

    car1.color = "blue"
    car2.status = "Ready"
    print(car1)
    print(car2)


if __name__ == "__main__":
    main()