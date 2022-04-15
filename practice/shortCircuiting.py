def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    inpList = list(map(int, input().split()))

    if len(inpList) == 3:
        if inpList[0] == inpList[1] == inpList[2]:
            print("equilateral")
        elif inpList[0] == inpList[1] or inpList[1] == inpList[2] or inpList[0] == inpList[2]:
            print("isosceles")
        else:
            print("scalene")
    return 0


if __name__ == '__main__':
    main()
