
from abc import ABC, abstractmethod
class apartment(ABC):
    def paySlip(self, amount):
        print("Monthly rent amount: ",amount)
# Passes an argument, hiding data
    @abstractmethod
    def payment(self, amount):
        pass

class WirePayment(apartment):
# Defines implementation of payment function from parent paySlip
    def payment(self, amount):
        print("Transfer amount of {} exceeds $500 limit ".format(amount))

obj = WirePayment()
obj.paySlip("$800")
obj.payment("$800")
