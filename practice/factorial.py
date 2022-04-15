def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    num = int(input())
    product = 1
    for i in range(1, num+1):
        product *= i
    print(product)
    return 0


if __name__ == '__main__':
    main()
