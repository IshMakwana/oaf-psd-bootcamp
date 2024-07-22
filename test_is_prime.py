import unittest
from is_prime import is_prime
# Unit test class
class TestIsPrime(unittest.TestCase):
     # Functional tests
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(97))
    
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(126))
    
    # Non-functional test to ensure the function can handle large numbers
    def test_large_is_prime(self):
        large_prime = 104729  
        self.assertTrue(is_prime(large_prime), f"{large_prime} should be prime")

    def test_large_is_non_prime(self):
        large_non_prime = 104730  
        self.assertFalse(is_prime(large_non_prime), f"{large_non_prime} should not be prime")

if __name__ == "__main__":
    unittest.main()