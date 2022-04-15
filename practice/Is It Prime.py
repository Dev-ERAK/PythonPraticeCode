def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    fCount = 0
    for i in range(2, N//2):
        if N % i == 0:
            fCount += 1

    if fCount == 0:
        print("YES")
    else:
        print("NO")

    return 0


if __name__ == '__main__':
    main()
