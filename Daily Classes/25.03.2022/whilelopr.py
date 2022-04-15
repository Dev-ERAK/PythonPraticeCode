n = int(input())
i = 1
count = 0

while i < n:
    x = i
    countI = 0
    while x > 0:
        #O(1) operation
        count += 1
        countI += 1

        x -= 1
    print("for : " + str(i) + ", count " + str(countI))
    i += 1

print(count)
