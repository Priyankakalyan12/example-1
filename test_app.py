#from app import Guvi
import app
import unittest


class Test_Collatz(unittest.TestCase):

        def test_Collatz1(self):
            self.assertEqual(app.Collatz_Conjenture(7),[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],"failed to find collatz Conjenture")
            

        def test_StepsToCollatz1(self):
            
            self.assertEqual(app.stepsToCollatzConjenture(app.Collatz_Conjenture(7)),17,"wrong steps")
            
# class Test_Example_File(unittest.TestCase):

#         def test_oddeven1(self):
#          self.assertEqual(app.Guvi(4),"even","expected num to be even")


         
if __name__ == '__main__':
    unittest.main()