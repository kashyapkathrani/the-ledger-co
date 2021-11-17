"""Contains requires Models"""
import math

class Loan:
    """Loan class with required attributes and functions"""

    def __init__(self, bank_name, borrower_name, principal, term, interest_rate):
        self.bank_name = bank_name
        self.borrower_name = borrower_name
        self.principal = principal
        self.term = term
        self.interest_rate = interest_rate
        self.lump_sum_payments = {}

    def get_total_repayment_amount(self):
        """The method returns total amount to be repaid"""

        interest = (self.principal*self.interest_rate*self.term)/100
        total_repayment_amount = self.principal + interest

        return total_repayment_amount

    def get_emi_amount(self):
        """The method returns emi amount"""

        total_repayment_amount = self.get_total_repayment_amount()
        emi_amount = math.ceil(float(total_repayment_amount)/(self.term*12))
        return emi_amount

    def add_lump_sum_payment(self, lump_sum_amount, no_of_emi):
        """The method adds lump sum payment"""

        if no_of_emi in self.lump_sum_payments:
            self.lump_sum_payments[no_of_emi] += lump_sum_amount
        else:
            self.lump_sum_payments[no_of_emi] = lump_sum_amount

    def get_balance(self, no_of_emi_paid):
        """The method returns amount paid and number of EMIs remaining"""

        emi_amount = self.get_emi_amount()
        amount_paid = no_of_emi_paid*emi_amount

        lump_sum_payment_keys = self.lump_sum_payments.keys()

        for emi_no in lump_sum_payment_keys:
            if emi_no <= no_of_emi_paid:
                amount_paid += self.lump_sum_payments[emi_no]

        total_repayment_amount = self.get_total_repayment_amount()

        if amount_paid > total_repayment_amount:
            amount_paid = total_repayment_amount

        amount_to_be_paid = total_repayment_amount - amount_paid

        no_of_emi_left = math.ceil(amount_to_be_paid/emi_amount)

        return {"amount_paid":int(amount_paid), "no_of_emi_left":int(no_of_emi_left)}
