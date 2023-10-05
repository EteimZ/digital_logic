import unittest
from digital.arithmetic import HalfAdder, FullAdder

class TestHalfAdder(unittest.TestCase):

    '''
    Inputs 	Outputs
    A 	B 	Cout 	S
    0 	0 	0 	    0
    0 	1 	0 	    1
    1 	0 	0 	    1
    1 	1 	1 	    0 
    '''

    def test_logic(self):
        a = HalfAdder.logic(0, 0)
        b = HalfAdder.logic(0, 1)
        c = HalfAdder.logic(1, 0)
        d = HalfAdder.logic(1, 1)
        
        self.assertEqual(a["sum"], 0)
        self.assertEqual(a["carry"], 0)

        self.assertEqual(b["sum"], 1)
        self.assertEqual(b["carry"], 0)

        self.assertEqual(c["sum"], 1)
        self.assertEqual(c["carry"], 0)

        self.assertEqual(d["sum"], 0)
        self.assertEqual(d["carry"], 1)
    
    def test_instance(self):
        a = HalfAdder(0, 0)
        b = HalfAdder(0, 1)
        c = HalfAdder(1, 0)
        d = HalfAdder(1, 1)

        self.assertEqual(a()["sum"], 0)
        self.assertEqual(a()["carry"], 0)

        self.assertEqual(b()["sum"], 1)
        self.assertEqual(b()["carry"], 0)

        self.assertEqual(c()["sum"], 1)
        self.assertEqual(c()["carry"], 0)

        self.assertEqual(d()["sum"], 0)
        self.assertEqual(d()["carry"], 1)
    
    def test_instance_call(self):
        a = HalfAdder()
        b = HalfAdder()
        c = HalfAdder()
        d = HalfAdder()

        self.assertEqual(a(0, 0)["sum"], 0)
        self.assertEqual(a(0, 0)["carry"], 0)

        self.assertEqual(b(0, 1)["sum"], 1)
        self.assertEqual(b(0, 1)["carry"], 0)

        self.assertEqual(c(1, 0)["sum"], 1)
        self.assertEqual(c(1, 0)["carry"], 0)

        self.assertEqual(d(1, 1)["sum"], 0)
        self.assertEqual(d(1, 1)["carry"], 1)

class TestFullAdder(unittest.TestCase):

    def test_logic(self):
        # Truth table values
        truth_table = [
            (0, 0, 0),  # A=0, B=0, Cin=0
            (0, 0, 1),  # A=0, B=0, Cin=1
            (0, 1, 0),  # A=0, B=1, Cin=0
            (0, 1, 1),  # A=0, B=1, Cin=1
            (1, 0, 0),  # A=1, B=0, Cin=0
            (1, 0, 1),  # A=1, B=0, Cin=1
            (1, 1, 0),  # A=1, B=1, Cin=0
            (1, 1, 1),  # A=1, B=1, Cin=1
        ]

        expected_results = [
            {"sum": 0, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 1},
        ]

        for i, (a, b, c) in enumerate(truth_table):
            result = FullAdder.logic(a, b, c)
            expected = expected_results[i]

            self.assertEqual(result["sum"], expected["sum"])
            self.assertEqual(result["carry"], expected["carry"])

    def test_instance(self):
        # Truth table values
        truth_table = [
            (0, 0, 0),  # A=0, B=0, Cin=0
            (0, 0, 1),  # A=0, B=0, Cin=1
            (0, 1, 0),  # A=0, B=1, Cin=0
            (0, 1, 1),  # A=0, B=1, Cin=1
            (1, 0, 0),  # A=1, B=0, Cin=0
            (1, 0, 1),  # A=1, B=0, Cin=1
            (1, 1, 0),  # A=1, B=1, Cin=0
            (1, 1, 1),  # A=1, B=1, Cin=1
        ]

        expected_results = [
            {"sum": 0, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 1},
        ]

        for i, (a, b, c) in enumerate(truth_table):
            adder = FullAdder(a, b, c)
            result = adder()
            expected = expected_results[i]

            self.assertEqual(result["sum"], expected["sum"])
            self.assertEqual(result["carry"], expected["carry"])

    def test_instance_call(self):
        # Truth table values
        truth_table = [
            (0, 0, 0),  # A=0, B=0, Cin=0
            (0, 0, 1),  # A=0, B=0, Cin=1
            (0, 1, 0),  # A=0, B=1, Cin=0
            (0, 1, 1),  # A=0, B=1, Cin=1
            (1, 0, 0),  # A=1, B=0, Cin=0
            (1, 0, 1),  # A=1, B=0, Cin=1
            (1, 1, 0),  # A=1, B=1, Cin=0
            (1, 1, 1),  # A=1, B=1, Cin=1
        ]

        expected_results = [
            {"sum": 0, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 0},
            {"sum": 0, "carry": 1},
            {"sum": 0, "carry": 1},
            {"sum": 1, "carry": 1},
        ]

        for i, (a, b, c) in enumerate(truth_table):
            adder = FullAdder()
            result = adder(a, b, c)
            expected = expected_results[i]

            self.assertEqual(result["sum"], expected["sum"])
            self.assertEqual(result["carry"], expected["carry"])

if __name__ == '__main__':
    unittest.main()