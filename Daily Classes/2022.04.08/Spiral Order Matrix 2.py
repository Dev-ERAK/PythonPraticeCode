def addRow(num, spiralMat, N, i, state):
    j = 0 if state == 0 else N - 1

    for _ in range(N):
        num += 1
        spiralMat[i][j] = num
        j = j + 1 if state == 0 else j - 1
    return num


def printMat(spiralMat):
    N = len(spiralMat)
    for i in range(N):
        for j in range(N):
            print(spiralMat[i][j], end=" ")
        print()


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    spiralMat = [[0] * N for _ in range(N)]

    num = 0
    i, j = 0, 0
    state = 0
    while i < N:
        num = addRow(num, spiralMat, N, i, state)
        i += 1
        state = 1 - state

    printMat(spiralMat)
    return 0


if __name__ == '__main__':
    main()
