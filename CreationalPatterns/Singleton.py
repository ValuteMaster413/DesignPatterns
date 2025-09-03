from random import randrange


class Car:
    _instance = None
    _initialized = False

    index = randrange(1, 10000)

    def __init__(self):
        if not Car._initialized:
            Car._initialized = True

    def __new__(cls):
        if not Car._instance:
            Car._instance = super().__new__(cls)
            return Car._instance
        else:
            return Car._instance


def main():
    car1 = Car()
    car2 = Car()

    print(f"{car1.index}, {car2.index}")


if __name__ == "__main__":
    main()
