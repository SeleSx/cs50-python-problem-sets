# prompt user for time, output breakfast/lunch/dinner time
# assume for 24 hour time #:## or ##:##
#7-8 breakfast, 12-13 lunch, 18-19 dinner

def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if "am" in time: #12 hour time, as is
        parts = time.split(" ")[0].split(":")
        hour = int(parts[0])
        minute = int(parts[1])
        #if hour is 12, make it 0
        if hour == 12:
            hour = 0

        time = round(hour + minute/60, 2)
        return time

    elif "pm" in time: #12 hour time, afternoon, add 12
        parts = time.split(" ")[0].split(":")
        hour = int(parts[0])
        minute = int(parts[1])
        # if hour is 12, let it be 12
        if hour != 12:
            hour += 12

        time = round(hour + minute/60, 2)
        return time

    else:
        parts = time.split(":")
        hour = int(parts[0])
        minute = int(parts[1])

        time = round(hour + minute/60, 2)
        return time


if __name__ == "__main__":
    main()