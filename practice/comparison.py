def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    count = int(input())
    arr = []
    i = 0
    for i in range(count):
        arr.append(input().replace(" ", ""))

    for item in arr:
        print(item)
    return 0


if __name__ == '__main__':
    main()
