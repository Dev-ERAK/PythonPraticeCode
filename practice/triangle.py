def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    Total = 0
    for i in range(1, A + 1):
        if i % 2 != 0:
            Total += i

    print(Total)

    return 0


if __name__ == '__main__':
    main()
