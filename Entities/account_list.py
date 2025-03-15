from  Entities.account import Account

class AccountList:
    def __init__(self , account_list=None):
        if account_list:
            self.account_list = account_list
        else:
            self.account_list = []
        self.show_account_list = self.account_list.copy()

    def search(self , term):
        self.show_account_list.clear()

        for account in self.account_list:
            if term in account.national_code or term in account.account_number:
                self.account_list.append(account)

    def insert(self, first_name, last_name, phone_number,
                 national_code, account_number, account_balance):
        new_id = len (self.account_list) +1
        new_account = Account (new_id , first_name, last_name, phone_number,
                 national_code, account_number, account_balance)

        self.account_list.append(new_account)
        self.show_account_list.append(new_account)

    def delete(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                self.account_list.remove(account)

        self.show_account_list = self.account_list.copy()


    def get_account(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account
