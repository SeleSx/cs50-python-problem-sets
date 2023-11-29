# YYYY-MM-DD
# input anno domini date, month day year, formatted like 9/8/1636 or september 8, 1636
# output date in YYYY-MM-DD
# if not valid, prompt again
# assume no month had over 31 days

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            dateIn = input("Date: ").strip()
            if "/" in dateIn:
                parts = dateIn.split("/")
                
                if int(parts[0]) > 12 or int(parts[0]) < 1 or int(parts[1]) > 31 or int(parts[1]) < 1:
                    raise ValueError

                month = "{:02d}".format(int(parts[0]))
                day = "{:02d}".format(int(parts[1]))
                year = "{:04d}".format(int(parts[2])) #leading zeroes four chars

                print(year + "-" + month + "-" + day)
                break

            elif "," in dateIn:
                parts = dateIn.split(",")[0].split(" ")
                parts.append(dateIn.split(",")[1])

                if int(months.index(parts[0])) > 12 or int(months.index(parts[0])) < 1 or int(parts[1]) > 31 or int(parts[1]) < 1:
                    raise ValueError
                
                month = "{:02d}".format(months.index(parts[0]) + 1)
                day = "{:02d}".format(int(parts[1]))
                year = "{:02d}".format(int(parts[2]))

                print(year + "-" + month + "-" + day)
                break 

            else:
                raise ValueError
            
        except ValueError:
            pass
            
main()