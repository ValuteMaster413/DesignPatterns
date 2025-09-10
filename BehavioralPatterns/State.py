from __future__ import annotations
from abc import ABC, abstractmethod
import threading


class Turnstile:
    def __init__(self) -> None:
        self.state = ClosedState()

    state: IState


class IState(ABC):
    @abstractmethod
    def insert_ticket(self, turnstile: Turnstile) -> None:
        pass
    @abstractmethod
    def pass_through(self, turnstile: Turnstile) -> None:
        pass
    @abstractmethod
    def complete_process(self, turnstile: Turnstile, success: bool = True) -> None:
        pass

class ClosedState(IState):
    def insert_ticket(self, turnstile: Turnstile) -> None:
        turnstile.state = ProcessingState()

    def pass_through(self, turnstile: Turnstile) -> None:
        print("Blocked")

    def complete_process(self, turnstile: Turnstile, success: bool = True) -> None:
        print("No process to complete")

class OpenState(IState):
    def __init__(self, turnstile):
        self.timer = threading.Timer(30, self.complete_process, args=[turnstile])
        self.timer.start()

    def insert_ticket(self, turnstile: Turnstile) -> None:
        print("Already Payed")

    def pass_through(self, turnstile: Turnstile) -> None:
        self.timer.cancel()
        turnstile.state = ClosedState()

    def complete_process(self, turnstile: Turnstile, success: bool = True) -> None:
        print("Time Is Up")
        turnstile.state = ClosedState()


class ProcessingState(IState):
    def insert_ticket(self, turnstile: Turnstile) -> None:
        print("Payment in processing")

    def pass_through(self, turnstile: Turnstile) -> None:
        print("Payment in processing")

    def complete_process(self, turnstile: Turnstile, success: bool = True) -> None:
        if success:
            print("Payment Successful! Turnstile opened.")
            turnstile.state = OpenState(turnstile)
        else:
            print("Payment Failed. Turnstile remains closed.")
            turnstile.state = ClosedState()


def main() -> None:
    turnstile = Turnstile()

    turnstile.state.pass_through(turnstile)

    turnstile.state.insert_ticket(turnstile)

    turnstile.state.complete_process(turnstile, success=True)

    turnstile.state.pass_through(turnstile)

    turnstile.state.insert_ticket(turnstile)

    turnstile.state.complete_process(turnstile, success=False)

    turnstile.state.pass_through(turnstile)


if __name__ == "__main__":
    main()