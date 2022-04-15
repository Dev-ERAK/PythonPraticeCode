def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    if N > 26:
        return
    if N >= 1:
        print("A")
    for i in range(2, N + 1):
        for j in range(i - 1):
            print(chr(64 + i), end=" ")
        print(chr(64 + i))
    return 0


if __name__ == '__main__':
    main()