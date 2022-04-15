n = int(input())
count = 0

for i in range(3, n // 3, 3):
    k = 0
    countI = 0
    for j in range(2, n // 2, 2):
        count += 1
        countI += 1
        k = j
    print("for : " + str(i) + ", count " + str(countI) + ", j= " + str(k))

print(count)
