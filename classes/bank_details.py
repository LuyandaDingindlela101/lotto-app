class BankingDetails:
    def __init__(self, acc_holder, acc_number, bank):
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.bank = bank

    #   __str__ FUNCTION IS TO PRINT A STRING VERSION OF THE CLASS
    def __str__(self):
        return "\n { account holder: " + self.acc_holder + ", " + "acc number: " + self.acc_number + ", " + "bank: " + self.bank + " } "

    #   MAKE A DICTIONARY FROM THE BankingDetails DETAILS
    def make_dict(self):
        return {
            "account holder": self.acc_holder,
            "account number": self.acc_number,
            "bank name": self.bank
        }
