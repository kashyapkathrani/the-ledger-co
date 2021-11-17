"""The entry of The Ledger Co."""
import sys
import processor

def route_input(input_line):
    """
        The function identifies the command and performs required actions
    """

    args = input_line.split() #spliting the input line to get arguments

    command = args[0] #identifying the command

    if command == "LOAN":

        #retrieving all the arguments required for adding loan
        bank_name = args[1]
        borrower_name = args[2]
        principal = int(args[3])
        term = int(args[4])
        interest_rate = int(args[5])

        #For adding loan calling add_loan method of processor module
        processor.add_loan(bank_name, borrower_name, principal, term, interest_rate)

    if command == "PAYMENT":

        #retrieving all the arguments required for adding payment
        bank_name = args[1]
        borrower_name = args[2]
        lump_sum_amount = int(args[3])
        no_of_emi = int(args[4])

        #For adding payment calling add_payment method of processor module
        processor.add_payment(bank_name, borrower_name, lump_sum_amount, no_of_emi)

    if command == "BALANCE":

        #retrieving all the arguments required for fetching loan balance
        bank_name = args[1]
        borrower_name = args[2]
        no_of_emi_paid = int(args[3])

        #For fetching loan balance calling get_balance method of processor module
        return processor.get_balance(bank_name, borrower_name, no_of_emi_paid)

    return None

if __name__ == "__main__":

    PATH = sys.argv[1] #retrieving path of text file

    #reading the text file
    FILE = open(PATH, "r")
    INPUT_LINES = FILE.readlines()

    for line in INPUT_LINES:
        route_input(line) #calling function to route input as required
