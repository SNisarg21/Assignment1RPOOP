import Abstract_code_bank

if __name__ == '__main__':
    dict = {}
    count = 1
    while True:
        print("1. Create New Account.")
        print("2. Get Account Details.")
        print("3. Withdraw Money.")
        print("4. Deposit Money.")
        print("5. Exit.")
        op = int(input(("Select any one option :")))
        if op == 1:
            Abstract_code_bank.Create().Create(count, dict)
            count += 1
        elif op == 2:
            Abstract_code_bank.accountDetail().accountDetail(dict)
        elif op == 3:
            Abstract_code_bank.money_withdraw().money_withdraw(dict)
        elif op == 4:
            Abstract_code_bank.money_deposit().money_deposit(dict)
        elif op == 5:
            print("Thankyou. Have a great day ahead!!")
            break
        else:
            print("Please enter correct choice!!")