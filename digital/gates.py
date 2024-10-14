from dataclasses import dataclass
from abc import ABC, abstractmethod

class GATE(ABC):

    @staticmethod
    @abstractmethod
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
    
    def __repr__(self):
        return f'{self.__class__.__name__}(A={self.A}, B={self.B}, result={self.logic(self.A, self.B)})'

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
    
    def __repr__(self):
        return f'{self.__class__.__name__}(A={self.A}, result={self.logic(self.A)})'

class NAND(BIGATE):

    @staticmethod
    def logic(a, b):
        return NOT.logic(AND.logic(a, b))

class XOR(BIGATE):

    @staticmethod
    def logic(a, b):
        andOutput = AND.logic(a, b)
        orOutput = OR.logic(a, b)

        notOutput = NOT.logic(andOutput)
        
        return AND.logic(notOutput, orOutput)

class XNOR(BIGATE):

    @staticmethod
    def logic(a, b):
        return NOT.logic(XOR.logic(a, b))
