# one coke 50 cents
# accept 25,10,5 cents

def main():
    remain = 50

    while remain > 0:
        print("Amount Due:", remain)
        insert = int(input("Insert Coin: "))
        if 50 % insert != 0 or insert == 50:
            continue
        remain = remain - insert

    print("Change Owed:", abs(remain))

main()