def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    # arrStr = input().strip().split(" ")
    arrStr = (
        100, 49, 82, 85, 38, 89, 66, 51, 4, 31, 12, 33, 83, 29, 64, 78, 50, 25, 24, 27, 76, 59, 65, 41, 37, 6, 80, 61,
        8,
        48, 38, 85, 41, 18, 12, 81, 36, 37, 12, 44, 22, 65, 12, 33, 19, 42, 25, 30, 5, 4, 96, 81, 72, 71, 20, 20, 23,
        85,
        93, 33, 32, 30, 12, 97, 24, 13, 93, 58, 74, 37, 10, 46, 26, 21, 41, 92, 90, 21, 65, 35, 89, 26, 10, 14, 64, 28,
        3,
        80, 99, 62, 38, 55, 8, 92, 31, 93, 58, 77, 21, 34, 57)
    outPutArr = []
    N = int(arrStr[0])

    for i in range(N, 0, -1):
        outPutArr.append(arrStr[i])

    for ele in outPutArr:
        print(ele, end=" ")
    return 0


if __name__ == '__main__':
    main()
