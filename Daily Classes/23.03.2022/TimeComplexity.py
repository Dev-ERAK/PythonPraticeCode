n = int(input())
k = 0
count = 0

for i in range(n // 2, n + 1):
    countI = 0
    j = 2
    while j <= n:
        count += 1
        countI += 1
        k = k + n // 2
        j = j * 2
    print("for : " + str(i) + ", count " + str(countI) + ", j= " + str(j))

#print(k)

print("Total count " + str(count))
