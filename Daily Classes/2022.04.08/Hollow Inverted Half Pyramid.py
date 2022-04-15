def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    space = " "
    for i in range(N, 1, -1):
        if i == N:
            print("*" * i)
        else:
            print("*" + (space * (i - 2)) + "*")
    if N >= 1:
        print("*")
    return 0


if __name__ == '__main__':
    main()
