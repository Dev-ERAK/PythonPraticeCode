def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    height = float(input("Enter the Height in cm : "));
    if height >= 195:
        print("abnormal");
    elif 195 > height >= 165:
        print("taller");
    elif 165 > height >= 150:
        print("average");
    else:
        print("dwarf");
    return 0


if __name__ == '__main__':
    main()
