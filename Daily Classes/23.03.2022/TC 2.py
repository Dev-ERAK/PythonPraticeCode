n = int(input())
i = n
count = 0
while i > 0:
    countI = 0
  #  print(i)
    k = 0
    if i % 2 == 0:
        for j in range(1, n * n + 1, 2):
            # O(1) operation
            count += 1
            countI += 1
            k = j

    print("for : " + str(i) + ", count " + str(countI) + ", j= " + str(k))
    i = i // 2

print("Total count " + str(count))

