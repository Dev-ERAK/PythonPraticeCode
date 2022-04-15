def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    B = int(input())
    result = 1
    for i in range(B):
        result = result * A
    print(result)
    return 0


if __name__ == '__main__':
    main()
