N = int(input())
num = N

flag = 0
if num < 0:
    flag = 1
    num *= -1
revNum = 0
while num:
    revNum = (revNum * 10) + (num % 10)
    num = num // 10

if flag:
    revNum *= -1

if revNum <= -2 ** 31 or revNum >= (2 ** 31 - 1):
    print(0)
else:
    print(revNum)

n = N
print(n)
SIZE = 4
pos = SIZE - 1  # maintains shift

# store reversed bits of `n`. Initially, all bits are set to 0
reverse = 0

# do till all bits are processed
while pos >= 0 and n:

    # if the current bit is 1, then set the corresponding bit in the result
    if n & 1:
        reverse = reverse ^ (1 << pos)

    n >>= 1  # drop current bit (divide by 2)
    pos = pos - 1  # decrement shift by 1

print(reverse)
