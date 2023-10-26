# E = mc^2, get m and output E

def main():
    m = int(input("m= "))
    print(convert(m))

def convert(m):
    return m * (300000000 ** 2)

main()