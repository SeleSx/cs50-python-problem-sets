def main():
    phrase = str(input())
    print(convert(phrase))

def convert(p):
    p = p.replace(":)", "🙂")
    p = p.replace(":(", "🙁")
    return p

main()