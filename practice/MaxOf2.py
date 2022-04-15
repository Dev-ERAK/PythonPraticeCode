def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    num1 = int(input())
    num2 = int(input())
    maxi = num1 if num1 > num2 else num2
    print(maxi)
    return 0


if __name__ == '__main__':
    main()
