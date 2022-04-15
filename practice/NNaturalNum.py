def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    num = int(input())
    i = 1
    while i <= num:
        print(i,end=" ")
        i += 1

    return 0


if __name__ == '__main__':
    main()