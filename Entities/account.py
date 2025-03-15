class Account:
    def __init__(self, id, first_name, last_name, phone_number,
                 national_code, account_number, account_balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.national_code = national_code
        self.account_number = account_number
        self.account_balance = account_balance

    def update(self, new_first_name, new_last_name, new_phone_number,
               new_national_code, new_account_number, new_account_balance):
        self.first_name = new_first_name
        self.last_name = new_last_name
        self.phone_number = new_phone_number
        self.national_code = new_national_code
        self.account_number = new_account_number
        self.account_balance = new_account_balance


    def deposit(self, amount):
        self.account_balance = self.account_balance + amount

    def withdrawal(self , amount):
        if amount < self.account_balance - 10:
            self.account_balance = self.account_balance - amount
        else:
            print("Your account balance is not enough.")

