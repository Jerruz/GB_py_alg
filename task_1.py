ls = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            ls[j - 2] += 1
i = 0
while i < len(ls):
    print(i + 2, ' - ', ls[i])
    i += 1
