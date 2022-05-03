from abc import ABC, abstractmethod

class bankAccount(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def Create(self, dict) -> None:
        pass

    @abstractmethod
    def accountDetail(self, dict) -> None:
        pass

    @abstractmethod
    def money_deposit(self, dict) -> None:
        pass

    @abstractmethod
    def money_withdraw(self, dict) -> None:
        pass



class Create(bankAccount):
    def accountDetail(self, dict) -> None:
        pass

    def money_deposit(self, dict) -> None:
        pass

    def money_withdraw(self, dict) -> None:
        pass

    def Create(self, count, dict):
            name = input("Enter the Name : ")
            def account_type(self):
                print("1. Savings Account.")
                print("2. Salary Account.")
                print("3. Current Account.")
                acc_type = int(input("Choose option number for account type :"))
                if acc_type == 1:
                    return "Savings Account"
                elif acc_type == 2:
                    return "Salary Account"
                elif acc_type == 3:
                    return "Current Account"
                else:
                    print("Please enter valid number")
                    account_type()
            print("Need to pay atleast 1000 rs to start")
            try:
                deposit = int(input("Enter Amount to be deposited : "))
                if deposit >= 1000:
                    balance = deposit
                    dict[count] = {}
                    dict[count]["Name :"] = name
                    dict[count]["Account Type :"] = account_type(self)
                    dict[count]["Account Number :"] = count + 100000
                    dict[count]["Balance :"] = balance
                    print("Account Successfully Created!!!!")
                    for key in dict[count]:
                        print(key, dict[count][key])
                else:
                    print("Deposit minimum of 1000 rs compulsory .... Start Process once Again!")
            except ValueError:
                print("Enter Amount Correctly ... Deposit minimum of 1000 rs compulsory .... Start Process once Again!")

class accountDetail(bankAccount): 

    def Create(self, dict) -> None:
        pass

    def money_deposit(self, dict) -> None:
        pass

    def money_withdraw(self, dict) -> None:
        pass

    def accountDetail(self, dict):
        val = int(input("Enter the account number : "))
        if val - 100000 not in dict:
            print("Enter Valid Account Number.")
        else:
            for key in dict[val - 100000]:
                print(key, dict[val - 100000][key])

class money_deposit(bankAccount):
    
    def Create(self, dict) -> None:
        pass

    def accountDetail(self, dict) -> None:
        pass

    def money_withdraw(self, dict) -> None:
        pass

    def money_deposit(self, dict):
        val = int(input("Enter the account number : "))
        if val - 100000 not in dict:
            print("Enter Valid Account Number.")
        else:
            money_deposit = int(input("Enter the money to be deposited :"))
            dict[val - 100000]["Balance :"] += money_deposit
            for key in dict[val - 100000]:
                print(key, dict[val - 100000][key])

class money_withdraw(bankAccount):

    def Create(self, dict) -> None:
        pass

    def accountDetail(self, dict) -> None:
        pass

    def money_deposit(self, dict) -> None:
        pass

    def money_withdraw(self, dict):
        val = int(input("Enter the account number : "))
        if val - 100000 not in dict:
            print("Enter Valid Account Number.")
        else:
            money_withdraw = int(input("Enter money to withdraw :"))
            if dict[val - 100000]["Balance :"] - money_withdraw >= 1000:
                            dict[val - 100000]["Balance :"] -= money_withdraw
                            for key in dict[val - 100000]:
                                print(key, dict[val - 100000][key])
            else:
                max_withdrawal = dict[val - 100000]["Balance :"]-1000
                print(f"Maximum of be {max_withdrawal} can withdrawed")
                print("Repeat the process once again!!")
