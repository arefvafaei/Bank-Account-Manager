####### Bank
from tkinter import Tk, Label, Button, Entry
from tkinter.ttk import Treeview
from Entities.account_list import AccountList
from Data.working_file import load_data, replace_data

login_form = Tk()
login_form.title("Login")

username_label = Label(login_form, text="Username:")
username_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

username_entry = Entry(login_form, width=50)
username_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="w")

password_label = Label(login_form, text="Password:")
password_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

password_entry = Entry(login_form, width=50)
password_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="w")


def login_submit():
    if username_entry.get()=="ADMIN".upper() and password_entry.get()=="123":

        login_form.destroy()

        account_list = load_data()

        account_list = AccountList(account_list)


        window = Tk()
        window.title("Bank Account Application")

        window.grid_rowconfigure(3, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
        window.grid_columnconfigure(2, weight=1)
        window.grid_columnconfigure(3, weight=1)


        def show_account_form(account=None):
            account_form = Tk()
            if account:
                account_form.title("Update Account")
            else:
                account_form.title("New Account")

            firstname_label = Label(account_form, text="First Name:")
            firstname_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

            firstname_entry = Entry(account_form, width=50)
            firstname_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="w")

            lastname_label = Label(account_form, text="Last Name:")
            lastname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

            lastname_entry = Entry(account_form, width=50)
            lastname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

            phone_label = Label(account_form, text="Phone Number:")
            phone_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

            phone_entry = Entry(account_form, width=50)
            phone_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

            code_label = Label(account_form, text="National Code:")
            code_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

            code_entry = Entry(account_form, width=50)
            code_entry.grid(row=3, column=1, pady=10, padx=(0, 10), sticky="w")

            account_number_label = Label(account_form, text="Account Number:")
            account_number_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

            account_number_entry = Entry(account_form, width=50)
            account_number_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

            balance_label = Label(account_form, text="Account Balance:")
            balance_label.grid(row=5, column=0, pady=(0, 10), padx=10, sticky="e")

            balance_entry = Entry(account_form, width=50)
            balance_entry.grid(row=5, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

            if account:
                firstname_entry.insert(0, account.first_name)
                lastname_entry.insert(0, account.last_name)
                phone_entry.insert(0, account.phone_number)
                code_entry.insert(0, account.national_code)
                account_number_entry.insert(0, account.account_number)
                balance_entry.insert(0, account.account_balance)

            def submit():
                firstname = firstname_entry.get()
                lastname = lastname_entry.get()
                phone = phone_entry.get()
                code = code_entry.get()
                account_number = account_number_entry.get()
                balance = balance_entry.get()

                if account:
                    account.update(firstname, lastname, phone, code, account_number, balance)
                    account_list.show_account_list = account_list.account_list.copy()
                else:
                    account_list.insert(firstname, lastname, phone, code, account_number, balance)

                load_data_treeview()
                replace_data(account_list.account_list)
                account_form.destroy()

            submit_button = Button(account_form, text="Submit", command=submit)
            submit_button.grid(row=6, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

            account_form.mainloop()


        def deposit():
                deposit_form = Tk()
                deposit_form.title("Deposit:")

                amount_label= Label(deposit_form, text="Amount")
                amount_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

                amount_entry=Entry(deposit_form, width=30)
                amount_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

                def submit():
                    amount = int(amount_entry.get())
                    account.deposit(amount)
                    account_list.show_account_list = account_list.account_list.copy()
                    replace_data(account_list.account_list)
                    load_data_treeview()
                    deposit_form.destroy()

                submit_button = Button(deposit_form, text="Submit", command=submit)
                submit_button.grid(row=1, column=1, pady=(0, 10), padx=10, sticky="w")

                load_data_treeview()

        def withdraw():
                withdrawal_form = Tk()
                withdrawal_form.title("Withdraw")

                amount_label = Label(withdrawal_form, text="Amount:")
                amount_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

                amount_entry = Entry(withdrawal_form, width=30)
                amount_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

                def submit():
                    amount = int(amount_entry.get())
                    account.withdraw(amount)
                    account_list.show_account_list = account_list.account_list.copy()
                    replace_data(account_list.account_list)
                    load_data_treeview()
                    withdrawal_form.destroy()

                submit_button = Button(withdrawal_form, text="Submit", command=submit)
                submit_button.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="w")

        insert_button = Button(window, text="New Account", command=show_account_form)
        insert_button.grid(row=0, column=0, pady=10, padx=10, sticky="e")


        def update_button_clicked():
            update_id = int(account_list_treeview.selection()[0])
            update_account = account_list.get_account(update_id)
            show_account_form(update_account)


        update_button = Button(window, text="Update Account" , command=update_button_clicked)
        update_button.grid(row=0, column=1, pady=10, padx=10)


        def delete_button_clicked():
            delete_rows = account_list_treeview.selection()

            for delete_row in delete_rows:
                delete_id = int(delete_row)
                account_list.delete(delete_id)

            replace_data(account_list.account_list)
            load_data_treeview()

        delete_button = Button(window, text="Delete Account", command=delete_button_clicked)
        delete_button.grid(row=0, column=2, pady=10, padx=10, sticky="w")


        def withdraw_button_clicked():
            withdraw_id = int(account_list_treeview.selection()[0])
            withdraw_account = account_list.get_account(withdraw_id)
            withdraw(withdraw_account)


        withdrawal_button = Button(window, text="Withdrawal" , command=withdraw_button_clicked)
        withdrawal_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")


        def deposit_button_clicked():
            deposit_id = int(account_list_treeview.selection()[0])
            deposit_account = account_list.get_account(deposit_id)
            deposit(deposit_account)


        deposit_button = Button(window, text="Deposit" , command=deposit_button_clicked)
        deposit_button.grid(row=1, column=1, pady=(0, 10), padx=10)





        def search_button_clicked():
            term = search_entry.get()

            account_list.search(term)

            load_data_treeview()


        search_entry = Entry(window)
        search_entry.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="ew")

        search_button = Button(window, text="Search" , command=search_button_clicked)
        search_button.grid(row=2, column=3, pady=(0, 10), padx=10, sticky="w" )

        account_list_treeview = Treeview(window,
                                         columns=("firstname", "lastname", "phone", "code", "account_number", "balance"))
        account_list_treeview.grid(row=3, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="nsew")

        account_list_treeview.heading("#0", text="NO.")
        account_list_treeview.heading("firstname", text="First Name")
        account_list_treeview.heading("lastname", text="Last Name")
        account_list_treeview.heading("phone", text="Phone Number")
        account_list_treeview.heading("code", text="National Code")
        account_list_treeview.heading("account_number", text="Account Number")
        account_list_treeview.heading("balance", text="Account Balance")

        account_list_treeview.column("#0", width=50)

        row_list = []


        def load_data_treeview():
            for row in row_list:
                account_list_treeview.delete(row)
            row_list.clear()

            account_data = account_list.show_account_list

            row_number = 1
            for account in account_data:
                row = account_list_treeview.insert("", "end", iid=account.id, text=str(row_number),
                                                   values=(account.first_name, account.last_name, account.phone_number,
                                                           account.national_code, account.account_number,
                                                           account.account_balance))

                row_list.append(row)
                row_number += 1


        def manage_button(event):
            select_count = len(account_list_treeview.selection())
            if select_count == 1:
                update_button.config(state="normal")
                delete_button.config(state="normal")
                withdrawal_button.config(state="normal")
                deposit_button.config(state="normal")
            elif select_count > 1:
                update_button.config(state="disabled")
                delete_button.config(state="normal")
                withdrawal_button.config(state="disabled")
                deposit_button.config(state="disabled")
            else:
                update_button.config(state="disabled")
                delete_button.config(state="disabled")
                withdrawal_button.config(state="disabled")
                deposit_button.config(state="disabled")

        account_list_treeview.bind("<<TreeviewSelect>>" , manage_button)

        window.mainloop()

login_submit_button = Button(login_form, text="Submit", command=login_submit)
login_submit_button.grid(row=2, column=1, pady=(0, 10), padx=10, sticky="w")

login_form.mainloop()