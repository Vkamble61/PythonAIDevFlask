import unittest

from mymodule import square, doubler, add

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2),4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

class TestDoubler(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(doubler(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(doubler(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(doubler(0), 0) # test when 0 is given as input the output is 0.

class TestAdd(unittest.TestCase): 
    def test3(self): 
        self.assertEqual(add(2,4), 6) # test when 2 & 4 is given as input the output is 6.
        self.assertEqual(add(0,0), 0) # test when 0 & 0 is given as input the output is 0.
        self.assertEqual(add(2.3, 3.6), 5.9) # test when 2.3 & 3.6 is given as input the output is 5.9.
        self.assertEqual(add('hello','world'), 'helloworld') # test when 'hello' & 'world' is given as input the output is helloworld.
        self.assertEqual(add(2.3000,4.300),6.6) # test when 0 & 0 is given as input the output is 6.6.
        self.assertNotEqual(add(-2, -2), 0) # test when 2.3 & 3.6 is given as input the output is not 0.     

unittest.main()    