import unittest
import test

class UnitTest(unittest.TestCase):

    def testp1(self):
        p1 = test.Problem1()
        p1.printNumbers()               

    def testp2(self):
        p2 = test.Problem1()
        p2.Dots("arrb6...4xxbl5...eee5")
        print p2


if __name__ == '__main__':
    unittest.main()