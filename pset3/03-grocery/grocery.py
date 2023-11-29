# prompt user for items one per line until ctrl + d
# output grocery list all uppercase, sorted alphabetically, prefixing each line with the num. of times the item was inputted
# treat input case-insensitively

def main():
    groceries = {}
    while True:
        try:
            item = input().strip()
            for c in item:
                if (not c.isalpha()) and c != " ":
                    raise ValueError
            
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        
        except ValueError:
            pass
        except EOFError:
            print()
            break
    
    groceriesSort = sorted(groceries) # returns list of keys sorted

    for i in groceriesSort:
        print(groceries[i], i.upper())

main()