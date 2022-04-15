def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input());
    B = int(input());
    C = int(input());

    if A < B:
        if A < C:
            print(A)
        else:
            print(C)
    else:
        if B < C:
            print(B)
        else:
            print(C)

    return 0

if __name__ == '__main__':
    main()