import sys


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    arrStr = input().strip().split(" ")

    N = int(arrStr[0])
    mini = sys.maxsize
    maxi = -sys.maxsize - 1

    for i in range(1, len(arrStr)):
        curr_Num = int(arrStr[i])
        if curr_Num > maxi:
            maxi = curr_Num

        if curr_Num < mini:
            mini = curr_Num

    print(str(maxi), end=" ")
    print(str(mini), end=" ")
    return 0


if __name__ == '__main__':
    main()
