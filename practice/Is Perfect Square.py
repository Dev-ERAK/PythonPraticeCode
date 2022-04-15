import math


def issquare(num):
    ans = None

    sqarValue = math.sqrt(num)
    print(sqarValue)
    ans = 0 if (sqarValue - math.floor(sqarValue)) != 0 else 1

    return ans


def main():
    N = int(input())

    for i in range(N):
        numb = int(input())
        print(issquare(numb))


if __name__ == '__main__':
    main()
