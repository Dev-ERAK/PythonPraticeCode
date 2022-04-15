def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    space = N - 1
    star = 1

    for i in range(1, N+1):
        print(" " * space, end="")
        for j in range(i):
            print("*", end=" ")
        print()
        space -= 1
    return 0


if __name__ == '__main__':
    main()
