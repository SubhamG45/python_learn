# atm project......
balance=15000

print("welcome to simple bank atm")
while True:
    input_text = """
what do you want to do?
1. check balance
2.deposit amount
3.withdraw amount
4.close program
:
    """
    user_input =int(input(input_text))
    if user_input==1:
        print(f"your balance is {balance}")
    elif user_input==2:
        amount=float(input("enter amount to deposit:"))
        balance+=amount
        print(f"successfully balanced. your balance is {balance}")
    elif user_input==3:
        amount=float(input("enter amount to withdraw:"))
        if balance>=amount:
            balance-=amount
            print(f"withdraw success.your new balance is {balance}")
        else:
            print("insufficient balance")
    elif user_input==4:
        print("thankyou for using simple bank atm.goodbye!")
        break
    else:
        print("invalid choice.try again")
