# can create by using abstract classes which have only abstract methods
from abc import ABC , abstractmethod
class Bank(ABC):
    def balance(self):
        pass
    def interest(self):
        pass
class Sbi(Bank):
    def balance(self):
        print('100 rupee')
    def interest(self):
        print('2 percent')
s=Sbi()
s.balance()
s.interest()