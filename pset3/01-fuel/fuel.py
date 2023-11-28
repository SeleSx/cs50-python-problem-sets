#input fraction X/Y, show percentage rounded to the nearest int
# if 1 or less, output E. if 99 or more, output F
# if X or Y not ints, X > Y, or Y is 0, prompt the user again
# be sure to catch ValueErrors or ZeroDivisionErrors


def main():
    print(get_percentage())


def get_percentage():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            if x > y:
                raise ValueError

            perc = round((x/y) * 100)

            
            
            if perc >= 99:
                return "F"
            elif perc <= 1:
                return "E"
            else:
                return str(perc) + "%"

        except (ValueError, ZeroDivisionError):
            pass

main()