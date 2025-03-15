from Entities.account import Account


def load_data():
    account_list = []
    with open("Data\\AccountData.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line_split = line.split(",")
            account = Account(int(line_split[0]), line_split[1], line_split[2], line_split[3],
                              line_split[4], line_split[5], line_split[6])
            account_list.append(account)

    return account_list


def replace_data(account_list):
    data_txt = ""
    last_account_item = account_list[-1]
    for account in account_list:
        data_txt += (f"{account.id},{account.first_name},{account.last_name},{account.phone_number},"
                     f"{account.national_code},{account.account_number},{account.account_balance}")
        if account.id != last_account_item.id:
            data_txt += "\n"

    with open("Data\\AccountData.txt", mode="w") as file:
        file.write(data_txt)
