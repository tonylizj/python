from Learn_to_Program_Crafting_Quality_Code import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_prices_summary here.
    def test_stock_prices_summary_normal(self):
        """
        test with generic number
        :return:
        """
        actual = a1.stock_prices_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_empty(self):
        """
        test with an empty list
        """
        actual = a1.stock_prices_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_no_losses(self):
        """
        test with no losses
        """
        actual = a1.stock_prices_summary([0.01, 0.03, 0.02, 0.14, 0, 0, 0.10, 0.01])
        expected = (0.31, 0)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_no_gains(self):
        """
        test with no gains
        """
        actual = a1.stock_prices_summary([-0.01, -0.03, -0.02, -0.14, -0, -0, -0.10, -0.01])
        expected = (0, -0.31)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_one_positive(self):
        """
        test with one positive item
        """
        actual = a1.stock_prices_summary([1])
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_one_negative(self):
        """
        test with one negative item
        """
        actual = a1.stock_prices_summary([-1])
        expected = (0, -1)
        self.assertEqual(expected, actual)

    def test_stock_prices_summary_one_0(self):
        """
        test with one zero
        """
        actual = a1.stock_prices_summary([0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
