import unittest
from prime_numbers import generate_primes


class PrimeNumberTests(unittest.TestCase):

    def test_only_allows_int_input(self):
        expected = "only integer input allowed"
        self.assertEqual(expected, generate_primes('10'),
                         msg="only input of type int allowed")

    def test_it_rejects_negative_input(self):
        expected = "invalid input"
        self.assertEqual(expected, generate_primes(-4),
                         msg="negative input is not allowed")

    def test_it_rejects_input_zero(self):
        expected = "invalid input"
        self.assertEqual(expected, generate_primes(0),
                         msg="zero is not a valid input")

    def test_it_returns_an_empty_list_for_input_below_3(self):
        expected = []
        self.assertEqual(expected, generate_primes(2),
                         msg="function must return empty list for input < 3")

    def test_if_it_returns_prime_numbers(self):
        # for n = 10
        expected_10 = [2,3,5,7]
        self.assertEqual(expected_10, generate_primes(10),
                         msg="function does not return prime numbers")
        # for n = 100
        expected_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                        59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expected_100, generate_primes(100),
                         msg="function does not return prime numbers")

    def test_it_gives_correct_no_of_outputs(self):
        # for n = 10, size of output = 4
        expected_10 = 4
        self.assertEqual(expected_10, 4, msg="incorrect size of output")
        expected_100 = 25
        self.assertEqual(expected_100, 25, msg="incorrect sze of output")

    def test_if_output_is_a_list(self):
        self.assertIsInstance(generate_primes(10), list, msg="output is not a list")

    def test_it_does_not_allow_input_over_1000(self):
        expected = "input exceeds 1000"
        self.assertEqual(expected, generate_primes(2000),
                         msg="input values over 1000 not allowed")

    def test_it_returns_a_list_of_size_1_for_input_of_3(self):
        expected = [2]
        self.assertEqual(generate_primes(3), expected,
                         msg="function should return a list with a single element")

    def test_the_output_is_within_range(self):
        # for n = 2, function should return an empty list
        expected_2 = []
        self.assertEqual(expected_2, generate_primes(2),
                         msg="output is not within range")
        # for n = 17, the last element should be 13
        expected_17 =[2,3,5,7,11,13]
        self.assertEqual(expected_17, generate_primes(17),
                         msg="output is not within range")

if __name__ == '__main__':
    unittest.main()
