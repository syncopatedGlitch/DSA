from abc import ABC, abstractmethod
from typing import Set

'''
use observer when multiple parts of the application
need to be updated abotu a change in one part of the
application.

Below is the example of the Stock market update oberver
pattern where a change in the price of a stock needs to
be updated to display service and the alarm service tracking
stock thresholds
'''


class Observer(ABC):

    @abstractmethod
    def update(self, symbol: str, price: float):
        pass


class Subject(ABC):
    '''
    You can chose to update observers about
    many different types of subjects. In this case, its
    stock, but it can equally be anything else as a subject
    '''
    def __init__(self) -> None:
        print("Base Subject init called")
        pass

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detatch(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observer(self, observer: Observer) -> None:
        pass


class Stock(Subject):
    def __init__(self, symbol: str) -> None:
        # super().__init__()
        self._observers: Set[Observer] = set()
        self.symbol = symbol
        self.price = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.add(observer)

    def detatch(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            print(f"No such observer for Subject: {self.__class__.__name__}")

    def set_price(self, price: float) -> None:
        self.price = price
        self.notify_observer(self.symbol, self.price)

    def notify_observer(self, symbol, price) -> None:
        for observer in self._observers:
            observer.update(symbol, price)


class PriceDisplay(Observer):
    def update(self, symbol: str, price: float) -> None:
        print(f"Display Updated: {symbol}: ${price}")


class PriceAlert(Observer):

    def __init__(self, threshold: float):
        self.threshold = threshold

    def update(self, symbol: str, price: float) -> None:
        if price > self.threshold:
            print(f"Stock crossed threshold: {symbol}: ${price}")


# Usage
stock = Stock("AAPL")

display = PriceDisplay()
alert = PriceAlert(150.00)
extra = PriceAlert(180.00)
stock.attach(display)
stock.attach(alert)

stock.set_price(145.00)  # Both observers get notified
stock.set_price(155.00)  # Both observers get notified
stock.detatch(extra)
