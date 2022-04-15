from math import sqrt


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(2, N + 1):
        if isPrime(i):
            print(i)

    return 0


def isPrime(num):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
