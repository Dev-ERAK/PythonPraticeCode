def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())

    for i in range(1, N + 1):
        for j in range(1, i):
            print(j, end=" ")
        print(i)
    return 0


if __name__ == '__main__':
    main()
