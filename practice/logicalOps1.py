def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input());
    B = int(input());
    C = int(input());

    maximum = A;
    if maximum < B:
        maximum = B;
    if maximum < C:
        maximum = C;

    print(maximum)
    return 0


if __name__ == '__main__':
    main()
