# vanity plates
# start with at least 2 letters
# contain max 6 chars and min 2 chars
# numbers must be at the end of the plate
# first number cannot be 0
# no periods, spaces or punctuation marks allowed

# assume input to be uppercase

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validity = True
    #check length
    if not (2 <= len(s) <= 6):
        validity = False
        #print("length")
    #check first two
    elif not s[0:2].isalpha():
        validity = False
        #print("first two not letters")
    #check az 19
    elif not s.isalnum():
        validity = False
        #print("az 19 issue")

    #if there's a number in plate
    if not s.isalpha():
        # get the first digit's index
        firstDigitIndex = 0
        for i in range(len(s)):
            if s[i].isdigit():
                firstDigitIndex = i
                break
    
        if s[firstDigitIndex] == "0":
            validity = False
            #print("first digit zero")

        elif not s[firstDigitIndex:].isnumeric():
            validity = False
            #print("letter after number?")
        
    return validity

main()