def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    inpList = list(map(int, input().split()))
    total = 0
    for item in inpList:
        total += item

    percentage = int(total / len(inpList))

    if percentage >= 90:
        print(str(percentage) + " A")
    elif percentage >= 80:
        print(str(percentage) + " B")
    elif percentage >= 70:
        print(str(percentage) + " C")
    elif percentage >= 60:
        print(str(percentage) + " D")
    elif percentage >= 40:
        print(str(percentage) + " E")
    else:
        print(str(percentage) + " F")

    return 0


if __name__ == '__main__':
    main()
