def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    tCase = int(input())

    while tCase:
        N = int(input())
        Num = N
        results = 0
        while Num:
            results = results * 10 + (Num % 10)
            Num = Num // 10

        print(results)
        tCase -= 1
    return 0


if __name__ == '__main__':
    main()
