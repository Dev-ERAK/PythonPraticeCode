def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    tc = int(input())
    myList = []
    while tc > 0:
        arrStr = input().strip().split(" ")
        arrStr.append(input())
        myList.append(arrStr)
        tc -= 1

    for key in myList:
        keyLastButOne = len(key) - 1
        print(search(key[1:keyLastButOne], int(key[keyLastButOne])))

    return 0


def search(arr, num):

    for ele in arr:
        if int(ele) == num:
            return 1
    return 0


if __name__ == '__main__':
    main()
