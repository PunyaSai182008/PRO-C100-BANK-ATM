class Atm:
    def __init__(self, card_no, pin):
        self.card_no = card_no
        self.pin = pin

    def cashwithdrawl(self, amount):
        new_amount = 10000-amount
        print("You Withdrawn: " + str(amount) + " Your remaining balance is: " + str(new_amount))

    def balanceinquiry(self):
        print("Your balance is: ₹10000")


def main():
    name = input("Enter your name: ")
    print("Hello, " + name)
    card_no = input("Enter your card number: ")
    pin = input("Enter your pin number: ")
    new_user = Atm(card_no, pin)

    print("Check Your Activity")
    print("1. Cash Withdrawl")
    print("2. Balance Inquiry")
    activity = int(input("Give your activity choice as 1 or 2 from above: "))

    if (activity == 1):
        amount = int(input("Enter the amount: "))
        new_user.cashwithdrawl(amount)
    elif (activity == 2):
        new_user.balanceinquiry()
    else:
        print("ENTER A VALID NUMBER")


if __name__ == "__main__":
    main()
