def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input())
    for i in range(1, A+1):
        total = 0
        for ch in str(i):
            total += (int(ch) ** 3)

        if total == i:
            print(i)
    return 0


if __name__ == '__main__':
    main()
