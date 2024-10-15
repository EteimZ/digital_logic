from .gates import AND, XOR, OR, NOT
from dataclasses import dataclass

#Reference implementation: http://www.csc.villanova.edu/~mdamian/Past/csc2400fa13/assign/ALU.html

@dataclass
class HalfAdder:
    A: bool = 0
    B: bool = 0
    
    @staticmethod
    def logic(a, b):
        xorSum = XOR.logic(a,b)
        carry  = AND.logic(a,b)

        return { "sum": xorSum, "carry": carry}

    def __call__(self, a=None, b=None):
        A = a if a != None else self.A
        B = b if b != None else self.B
        return self.logic(A, B)

@dataclass
class FullAdder:
    A: bool = 0
    B: bool = 0
    C: bool = 0
    
    @staticmethod
    def logic(a, b, c):
        firstAdder = HalfAdder.logic(a, b)
        SecondAdder = HalfAdder.logic(firstAdder["sum"], c)

        orResult = OR.logic(firstAdder["carry"], SecondAdder["carry"])
        return {"sum": SecondAdder["sum"], "carry": orResult}

    def __call__(self, a=None, b=None, c=None):
        A = a if a != None else self.A
        B = b if b != None else self.B
        C = c if c != None else self.C
        return self.logic(A, B, C)


@dataclass
class NBitAdder:
    A: list[bool]
    B: list[bool]
    n: int = 8 # Add case to prevent one bit

    @staticmethod
    def logic(a: list[bool], b:list[bool], n=8):

        if n <= 1:
            raise ValueError("n cannot be less than or equal to one")
        
        if isinstance(a, list) == False or isinstance(b, list)  == False:
            raise ValueError("Inputs should be a list")
        
        if len(a) < n or len(b) < n:
            raise ValueError("Input list cannot be less than n")
        
        full_result = []
        
        result = HalfAdder.logic(a[n-1], b[n-1])
        
        full_result.append(result["sum"])
        for i in reversed(range(n-1)):
            result = FullAdder.logic(a[i], b[i], result["carry"])
            full_result.append(result["sum"])
        
        # Sanitize result: ensure it is always 1s and 0s
        result = int(bool(result["carry"]))
        
        full_result.append(result)
        full_result.reverse()
        return full_result
    
    def __call__(self, a, b, n):
        A = a if a != None else self.A
        B = b if b != None else self.B
        return self.logic(A, B, n)

@dataclass
class HalfSubstractor:
    A: bool = 0
    B: bool = 0
    
    @staticmethod
    def logic(a, b):
        xorSub = XOR.logic(a,b)

        notOut = NOT.logic(a)
        andOut = AND.logic(notOut, b)

        return {"sub": xorSub, "remainder": andOut}

    def __call__(self, a=None, b=None):
        A = a if a != None else self.A
        B = b if b != None else self.B
        return self.logic(A, B)

@dataclass
class FullSubstractor:
    A: bool = 0
    B: bool = 0
    C: bool = 0 

    @staticmethod
    def logic(a, b, c):
        firstSubstractor = HalfSubstractor.logic(a, b)
        SecondSubstractor = HalfSubstractor.logic(firstSubstractor["sub"], c)

        orResult = OR.logic(firstSubstractor["remainder"], SecondSubstractor["remainder"])
        return {"sub": SecondSubstractor["sub"], "remainder": orResult}

    def __call__(self, a=None, b=None, c=None):
        A = a if a != None else self.A
        B = b if b != None else self.B
        C = c if c != None else self.C
        return self.logic(A, B, C)
    
@dataclass
class NBitSubstractor:
    A: list[bool]
    B: list[bool]
    n: int = 8 # Add case to prevent one bit

    @staticmethod
    def logic(a: list[bool], b:list[bool], n=8):

        if n <= 1:
            raise ValueError("n cannot be less than or equal to one")
        
        if isinstance(a, list) == False or isinstance(b, list)  == False:
            raise ValueError("Inputs should be a list")
        
        if len(a) < n or len(b) < n:
            raise ValueError("Input list cannot be less than n")

        full_result = []
        
        result = HalfSubstractor.logic(a[n-1], b[n-1])
        
        full_result.append(result["sub"])
        for i in reversed(range(n-1)):
            result = FullSubstractor.logic(a[i], b[i], result["remainder"])
            full_result.append(result["sub"])

        result = int(bool(result["remainder"]))
        
        full_result.append(result)
        full_result.reverse()
        return full_result
    
    def __call__(self, a, b, n):
        A = a if a != None else self.A
        B = b if b != None else self.B
        return self.logic(A, B, n)




# ha = HalfAdder()
# print(ha(1,1))

# fa = FullAdder()
# print(fa(1,1,1))

# a = [1, 1, 1, 1, 1, 1, 1, 1 ]
# b = [1, 1, 1, 1, 1, 1, 1, 1 ]
# print(NBitAdder.logic(a, b, 2))
        
# print(HalfSubstractor.logic(0,0))
# print(HalfSubstractor.logic(0,1))
# print(HalfSubstractor.logic(1,0))
# print(HalfSubstractor.logic(1,1))
