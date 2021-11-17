"""Module helps in adding loan, adding payment and fetching balance"""

from models import Loan

LOANS = {}

def get_loan_identifier(bank_name, borrower_name):
    """The method returns the unique identifier for a loan"""

    return bank_name+"_"+borrower_name

def add_loan(bank_name, borrower_name, principal, term, interest_rate):
    """The method is use to add a loan"""

    loan = Loan(bank_name, borrower_name, principal, term, interest_rate)

    identifier = get_loan_identifier(bank_name, borrower_name)
    LOANS[identifier] = loan

def add_payment(bank_name, borrower_name, lump_sum_amount, no_of_emi):
    """The method is use to add a lump sum payment"""

    identifier = get_loan_identifier(bank_name, borrower_name)
    try:
        loan = LOANS[identifier]
    except:
        raise Exception("Error - No such loan exists")

    loan.add_lump_sum_payment(lump_sum_amount, no_of_emi)

def get_balance(bank_name, borrower_name, no_of_emi_paid):
    """The method is use to fetch amount paid and number of EMIs remaining"""

    identifier = get_loan_identifier(bank_name, borrower_name)
    try:
        loan = LOANS[identifier]
    except:
        raise Exception("Error - No such loan exists")

    response = loan.get_balance(no_of_emi_paid)

    output_format = bank_name+" "+borrower_name+" "
    output_format += str(response["amount_paid"])+" "+str(response["no_of_emi_left"])
    print(output_format)

    return response
