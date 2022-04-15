N = int(input())
count = 0
for i in range(2 ** N):
    j = i
    k = 0
    countI = 0
    while j > 0:
        count += 1
        countI += 1
        j -= 1
        k = j
    print("for : " + str(i) + ", count " + str(countI) + ", j= " + str(k))

print(count)
