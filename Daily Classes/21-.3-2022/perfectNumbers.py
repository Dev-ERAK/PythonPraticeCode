def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    N = int(input())
    resList = list()
    for i in range(N):
        A = int(input())
        total = 0
        for k in range(1, A):
            if A % k == 0:
                total += k

        if total == A:
            resList.append("YES")
        else:
            resList.append("NO")

    for i in resList:
        print(i)
    return 0


if __name__ == '__main__':
    main()
