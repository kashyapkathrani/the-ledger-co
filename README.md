# the-ledger-co
Code for The Ledger Co. by GeekTrust.

Command to run
python geektrust.py deserveTestCase.txt

Output
IDIDI Dale UPDATED EMI AMOUNT 227.0 UPDATED REPAYMENT AMOUNT 12464.4

The changes are made in models.py file.

I have added make_interest_change() function which calculates,
 - Amount paid before interest change
 - Remaining Prinicipal Amount
 - new Repayment amount based on new interest rate and Remaining Prinicipal Amount
 - new EMI amount.

PS - The calculations done during the interview are in note.txt
