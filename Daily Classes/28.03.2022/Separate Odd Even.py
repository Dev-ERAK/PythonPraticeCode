def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    tCases = int(input())

    outputArray = []
    while tCases > 0:
        myOddList = []
        myEvenList = []
        N = int(input())
        myList = list(map(int, input().split()))

        for ele in myList:
            if ele % 2 == 0:
                myEvenList.append(ele)
            else:
                myOddList.append(ele)

        for ele in myOddList:
            print(ele, end=' ')
        print()
        for ele in myEvenList:
            print(ele, end=' ')
        print()

        tCases -= 1

    return 0


if __name__ == '__main__':
    main()
