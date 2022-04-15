def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    N = int(input())
    star = "*"
    space = " "
    spm = 0
    stm = N
    for i in range(2 * N):
        print(star * stm + space * spm + space * spm + star * stm)

        if i == N - 1:
            continue

        if i < N:
            spm += 1
            stm -= 1
        else:
            spm -= 1
            stm += 1

    return 0


if __name__ == '__main__':
    main()
