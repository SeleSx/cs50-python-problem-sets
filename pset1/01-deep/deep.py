def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if ans.strip(" ") == "42" or ans.lower().replace("-", " ") == "forty two":
        print("Yes")
    else:
        print("No")
main()