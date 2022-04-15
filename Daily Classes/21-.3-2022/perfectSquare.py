from math import sqrt


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input())

    low = 1
    high = A
    mid = int(A/2)
    print(mid)
    while low <= high:
        if mid * mid == A:
            return mid
            break
        elif mid * mid < A:
            low = mid + 1
        else:
            high = mid - 1

        mid = int((high + low + 1) / 2)
        print(mid)

    return -1


if __name__ == '__main__':
    main()
