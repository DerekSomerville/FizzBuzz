import unittest
from python.src.FizzBuzz import fizzBuzz

class test_FizzBuss(unittest.TestCase):

    def test_number(self):
        self.assertEqual(fizzBuzz(2),"2")

    def test_FizzThree(self):
        self.assertEqual(fizzBuzz(3),"Fizz")

    def test_FizzSix(self):
        self.assertEqual(fizzBuzz(6),"Fizz")

    def test_BuzzFive(self):
        self.assertEqual(fizzBuzz(5),"Buzz")

    def test_BuzzTen(self):
        self.assertEqual(fizzBuzz(10),"Buzz")

    def test_FizzAndBuzzFifteen(self):
        self.assertEqual(fizzBuzz(15),"FizzBuzz")

    def main():
        unittest.main()

if __name__ == "__main__":
    unittest.main()
