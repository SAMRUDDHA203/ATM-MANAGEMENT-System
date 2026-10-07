import time

data = {
    "pin":"1234",
    "balance":1000,
    "history":[]
}


def checkpin():

    a=3

    while a>0:
        p=input("Enter your pin : ")

        if p==data["pin"]:
            print("pin correct")
            return True
        else:
            a=a-1
            print("wrong pin")
            print("tries left",a)

    print("account locked")
    return False


def balance():
    print("\nBalance")
    print("your balance is $",data["balance"])


def deposit():

    try:
        x=float(input("Enter amount : "))

        if x>0:
            data["balance"]=data["balance"]+x
            data["history"].append("Deposit : $"+str(x))
            print("deposited")
            print("balance =",data["balance"])
        else:
            print("amount should be greater than 0")

    except ValueError:
        print("invalid amount")


def withdraw():

    try:
        x=float(input("Enter amount to withdraw : "))

        if x<=0:
            print("wrong amount")

        elif x>data["balance"]:
            print("you dont have enough money")

        else:
            data["balance"]=data["balance"]-x
            data["history"].append("Withdraw : $"+str(x))
            print("withdraw successful")
            print("balance =",data["balance"])

    except ValueError:
        print("enter number only")


def history():

    print("\nHistory")

    if len(data["history"])==0:
        print("nothing here")

    else:
        for i in data["history"]:
            print(i)


def start():

    ok=checkpin()

    if ok==False:
        return

    while True:

        print("\n")
        print("******** ATM ********")
        print("1 balance")
        print("2 deposit")
        print("3 withdraw")
        print("4 history")
        print("5 exit")

        ch=input("enter your choice : ")

        if ch=="1":
            balance()

        elif ch=="2":
            deposit()

        elif ch=="3":
            withdraw()

        elif ch=="4":
            history()

        elif ch=="5":
            print("Thank you")
            break

        else:
            print("invalid choice")

        time.sleep(1)


start()