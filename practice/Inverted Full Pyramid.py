def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    space = 0
    star = 1

    for i in range(0, N):
        print(" " * space, end="")
        for j in range(N, i, -1):
            print("*", end=" ")
        print()
        space += 1
    return 0


if __name__ == '__main__':
    main()
