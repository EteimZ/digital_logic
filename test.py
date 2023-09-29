import unittest
from main import AND, OR, NOT, NAND, XOR, XNOR

class TestAND(unittest.TestCase):

    def test_logic(self):
        a = AND.logic(1, 1)
        b = AND.logic(1, 0)
        c = AND.logic(0, 1)
        d = AND.logic(0, 0)

        self.assertTrue(a)
        self.assertFalse(b)
        self.assertFalse(c)
        self.assertFalse(d)
    
    def test_instance(self):
        a = AND(1, 1)
        b = AND(1, 0)
        c = AND(0, 1)
        d = AND(0, 0)

        self.assertTrue(a())
        self.assertFalse(b())
        self.assertFalse(c())
        self.assertFalse(d())

    def test_instance_call(self):
        a = AND()
        b = AND()
        c = AND()
        d = AND()

        self.assertTrue(a(1, 1))
        self.assertFalse(b(1, 0))
        self.assertFalse(c(0, 1))
        self.assertFalse(d(0, 0))

class TestOR(unittest.TestCase):

    def test_logic(self):
        a = OR.logic(1, 1)
        b = OR.logic(1, 0)
        c = OR.logic(0, 1)
        d = OR.logic(0, 0)

        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertFalse(d)

    def test_instance(self):
        a = OR(1, 1)
        b = OR(1, 0)
        c = OR(0, 1)
        d = OR(0, 0)

        self.assertTrue(a())
        self.assertTrue(b())
        self.assertTrue(c())
        self.assertFalse(d())

    def test_instance_call(self):
        a = OR()
        b = OR()
        c = OR()
        d = OR()

        self.assertTrue(a(1, 1))
        self.assertTrue(b(1, 0))
        self.assertTrue(c(0, 1))
        self.assertFalse(d(0, 0))

class TestNOT(unittest.TestCase):

    def test_logic(self):
        a = NOT.logic(1)
        b = NOT.logic(0)

        self.assertFalse(a)
        self.assertTrue(b)

    def test_instance(self):
        a = NOT(1)
        b = NOT(0)

        self.assertFalse(a())
        self.assertTrue(b())

    def test_instance_call(self):
        a = NOT()
        b = NOT()

        self.assertFalse(a(1))
        self.assertTrue(b(0))

class TestNAND(unittest.TestCase):

    def test_logic(self):
        a = NAND.logic(1, 1)
        b = NAND.logic(1, 0)
        c = NAND.logic(0, 1)
        d = NAND.logic(0, 0)

        self.assertFalse(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertTrue(d)

    def test_instance(self):
        a = NAND(1, 1)
        b = NAND(1, 0)
        c = NAND(0, 1)
        d = NAND(0, 0)

        self.assertFalse(a())
        self.assertTrue(b())
        self.assertTrue(c())
        self.assertTrue(d())

    def test_instance_call(self):
        a = NAND()
        b = NAND()
        c = NAND()
        d = NAND()

        self.assertFalse(a(1, 1))
        self.assertTrue(b(1, 0))
        self.assertTrue(c(0, 1))
        self.assertTrue(d(0, 0))

class TestXOR(unittest.TestCase):

    def test_logic(self):
        a = XOR.logic(1, 1)
        b = XOR.logic(1, 0)
        c = XOR.logic(0, 1)
        d = XOR.logic(0, 0)

        self.assertFalse(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertFalse(d)

    def test_instance(self):
        a = XOR(1, 1)
        b = XOR(1, 0)
        c = XOR(0, 1)
        d = XOR(0, 0)

        self.assertFalse(a())
        self.assertTrue(b())
        self.assertTrue(c())
        self.assertFalse(d())

    def test_instance_call(self):
        a = XOR()
        b = XOR()
        c = XOR()
        d = XOR()

        self.assertFalse(a(1, 1))
        self.assertTrue(b(1, 0))
        self.assertTrue(c(0, 1))
        self.assertFalse(d(0, 0))

class TestXNOR(unittest.TestCase):

    def test_logic(self):
        a = XNOR.logic(1, 1)
        b = XNOR.logic(1, 0)
        c = XNOR.logic(0, 1)
        d = XNOR.logic(0, 0)

        self.assertTrue(a)
        self.assertFalse(b)
        self.assertFalse(c)
        self.assertTrue(d)

    def test_instance(self):
        a = XNOR(1, 1)
        b = XNOR(1, 0)
        c = XNOR(0, 1)
        d = XNOR(0, 0)

        self.assertTrue(a())
        self.assertFalse(b())
        self.assertFalse(c())
        self.assertTrue(d())


    def test_instance_call(self):
        a = XNOR()
        b = XNOR()
        c = XNOR()
        d = XNOR()

        self.assertTrue(a(1, 1))
        self.assertFalse(b(1, 0))
        self.assertFalse(c(0, 1))
        self.assertTrue(d(0, 0))


if __name__ == '__main__':
    unittest.main()
