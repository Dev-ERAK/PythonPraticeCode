def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arrStr = input().strip().split(" ")
    B = int(input())

    outPutArr = []
    N = int(arrStr[0])
    B = B % N
    
    for i in range(1, B + 1):
        outPutArr.append(arrStr[N - B + i])

    for i in range(1, N - B + 1):
        outPutArr.append(arrStr[i])

    for ele in outPutArr:
        print(ele, end=" ")
    return 0


if __name__ == '__main__':
    main()
