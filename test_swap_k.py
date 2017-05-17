import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_normal(self):
        """
        test with generic list and number
        """
        L = [1, 2, 3, 4, 5, 6]
        k = 2
        a1.swap_k(L, k)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_0(self):
        """
        test with k as 0
        """
        L = [1, 2, 3, 4, 5, 6]
        k = 0
        a1.swap_k(L, k)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(L, expected)

    def test_swap_k_empty(self):
        """
        test with empty list
        """
        L = []
        k = 2
        a1.swap_k(L, k)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_half_length(self):
        """
        test with k as half the length (highest possible)
        """
        L = [1, 2, 3, 4, 5, 6]
        k = 3
        a1.swap_k(L, k)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(L, expected)

    def test_swap_k_1(self):
        """
        test with k as 1 (lowest possible)
        """
        L = [1, 2, 3, 4, 5, 6]
        k = 1
        a1.swap_k(L, k)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(L, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
