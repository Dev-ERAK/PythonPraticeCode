import math


def getFibonacci(numb):
    a = 0
    b = 1

    if numb == 0:
        return 0
    elif numb == 1:
        return 1

    for i in range(numb - 1):
        c = a + b
        a = b
        b = c
        math.pi

        math.
    return c


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    print(getFibonacci(N))

    return 0


if __name__ == '__main__':
    main()
