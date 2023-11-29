#prompt user for orders one per line until ctrl+d
# after this, display total cost prefixed with $ formatted to 2 decimal places
# case insensitive, ignore any input that isn't an item
# assume every item on the menu to be titlecased


taq = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0

    while True:
        try:
            order = input("Item: ").lower().title().strip()
            total += taq[order]
            print("Total: ${0:.2f}".format(total))
        
        except EOFError:
            print()
            break
        except ValueError:
            pass
        except KeyError:
            pass

main()