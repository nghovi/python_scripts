#!/usr/bin/python
import unittest
import number

def test_number_fib():
    unittest.TestCase.assertEqual(number.fib(3), [1, 2, 3])
    unittest.TestCase.assertEqual(number.fib(1), [1])

def test_is_prime():
    unittest.TestCase.assertEqual(number.is_prime(0), True)
    unittest.TestCase.assertEqual(number.is_prime(1), True)
    unittest.TestCase.assertEqual(number.is_prime(2), True)
    unittest.TestCase.assertEqual(number.is_prime(3), False)
    unittest.TestCase.assertEqual(number.is_prime(19), False)
    unittest.TestCase.assertEqual(number.is_prime(-6), False)

if __name__ == '__main__':
    unittest.TestCase.assertEqual(1,2)