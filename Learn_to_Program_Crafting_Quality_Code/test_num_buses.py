from Learn_to_Program_Crafting_Quality_Code import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_normal(self):
        """
        test with generic number
        """
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_1(self):
        """
        test with 1 passenger
        """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_0(self):
        """
        test with no passengers (lowest possible)
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_divisible(self):
        """
        test with passengers that fit exactly into 50
        """
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_divisibleplus1(self):
        """
        test with passengers that fit exactly into 50 plus 1
        """
        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
