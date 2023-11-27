def main():
    camel = input("camelCase: ")

    print(convert(camel))

def convert(camel):
    snake = ""
    for i in camel:
        if i.isupper():
            snake += ("_" + i.lower())
        else:
            snake += i
    return snake

main()