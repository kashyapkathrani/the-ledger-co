"""File for Unit Testing"""

import unittest
import processor
import geektrust

class TestMethods(unittest.TestCase):
    """Class for Unit Testing geektrust module"""

    def test_route_input_add_loan(self):
        """Testing route_input function for adding loan"""
        geektrust.route_input('LOAN IDIDI John 20000 4 5')

        identifier = processor.get_loan_identifier("IDIDI", "John")
        principal = processor.LOANS[identifier].principal

        self.assertEqual(principal, 20000)

    def test_route_input_add_payment(self):
        """Testing route_input function for adding payment"""
        geektrust.route_input('LOAN IDIDI John 20000 4 5')
        geektrust.route_input('PAYMENT IDIDI John 500 6')

        identifier = processor.get_loan_identifier("IDIDI", "John")
        lump_sum_payments = processor.LOANS[identifier].lump_sum_payments

        self.assertEqual(lump_sum_payments[6], 500)

    def test_route_input_get_balance(self):
        """Testing route_input function for fetching balance"""
        geektrust.route_input('LOAN IDIDI John 20000 4 5')
        response = geektrust.route_input('BALANCE IDIDI John 5')

        self.assertEqual(response['amount_paid'], 2500)
        self.assertEqual(response['no_of_emi_left'], 43)


if __name__ == '__main__':
    unittest.main()
