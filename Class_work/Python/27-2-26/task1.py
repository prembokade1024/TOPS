# task_1................
l = [26,42,11,24,21,11]
uni = []
dup = []
for i in range (len(l)):
    j = l[i]
    if j not in uni:
        uni.append(j)
    else:
        dup.append(uni.index(j))
        dup.append(i)

print(dup)