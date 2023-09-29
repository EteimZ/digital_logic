from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod, abstractstaticmethod

class GATE(ABC):
    
    @abstractstaticmethod
    def logic(self):
        pass

@dataclass
class BIGATE(GATE, ABC):
    A: bool = 0
    B: bool = 0 

    def __call__(self, a=None, b=None):
        A = a if a != None else self.A
        B = b if b != None else self.B
        return self.logic(A, B)

class AND(BIGATE):
   
    @staticmethod
    def logic(a, b):
        return a and b
        
class OR(BIGATE):

    @staticmethod
    def logic(a, b):
        return a or b

@dataclass
class NOT(GATE):
    A: bool = 0

    @staticmethod
    def logic(a):
        return int(not a)

    def __call__(self, a=None):
        A = a if a != None else self.A
        return int(not A)

@dataclass
class NAND(BIGATE):

    @staticmethod
    def logic(a, b):
        return NOT.logic(AND.logic(a, b))

@dataclass
class XOR(BIGATE):

    @staticmethod
    def logic(a, b):
        if a == b:
            return 0
        else:
            return 1

@dataclass
class XNOR(BIGATE):

    @staticmethod
    def logic(a, b):
        return NOT.logic(XOR.logic(a, b))
