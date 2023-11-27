# omit vowels

def main():
    original = input("Input: ")
    print(convert(original))

def convert(original):
    vowels = "aeiou"
    converted = ""
    for i in original.strip():
        if i.lower() in vowels:
            continue
        converted += i
    return converted

main()